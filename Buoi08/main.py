from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: Annotated[int | None, Field(primary_key=True)] = None
    name: str
    secret_name: str
    age: Annotated[int | None, Field(default=None)] = None
    
class User(SQLModel, table=True):
    id: Annotated[int | None, Field(primary_key=True)] = None
    name: str
    email: str
    password: str
    role: str