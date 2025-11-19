from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = Field(default=None)
    
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    role: str
    
class Loai(SQLModel, table=True):    
    MaLoai: int | None = Field(default=None, primary_key=True)
    TenLoai: str = Field(index=True)

class HangHoa(SQLModel, table=True):    
    MaHH: int | None = Field(default=None, primary_key=True)
    TenHH: str = Field(index=True)
    Hinh: str = Field()
    MaLoai: int | None =  Field(foreign_key="loai.MaLoai")
    
# PyMySQL
engine = create_engine("mysql+pymysql://root:@localhost/2521comp180401", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Hello World"}
    
@app.get("/heroes/")
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes

@app.post("/heroes/", response_model=Hero)
def create_hero(*, session: SessionDep, hero: Hero):
    print("Entry", hero)
    session.add(hero)
    session.commit()
    session.refresh(hero)
    print("Exit", hero)
    return hero