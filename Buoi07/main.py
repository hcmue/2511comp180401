from fastapi import  FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
import json
from pydantic import BaseModel
from fastapi import UploadFile
import shutil
import os


app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello world"}

def load_students():
    try:
        with open("students.json", "r", encoding="utf8") as mf:
            return json.load(mf)
    except Exception as ex:
        print(ex)
        return []

def get_student_by_id(id):
    data = load_students()  
    for student in data:
        if student["id"] == id:
            return student
    return None

class Student(BaseModel):
    id: str
    name: str
    mark: float
    gpa: str

@app.get("/students")
def get_students():
    return load_students()

@app.get("/students/{id}")
def get_students(id:int):
    student = get_student_by_id(id)
    if student is not None:
        return student
    raise HTTPException(
            status_code=404,
            detail=f"Not found {id}",
        )

@app.post("/students")
def create_new_student(model: Student):
    student = get_student_by_id(model.id)
    if student is not None:
        raise HTTPException(
                status_code=400,                
                detail=f"Student {model.id} is existed",
            )
    # Save


# from fastapi.responses import HTMLResponse
@app.get("/hello", response_class=HTMLResponse)
def hello():
    return "<html><head></head><body><h1>HELLO</h1></body></html>"


# from fastapi import UploadFile
# import shutil
# Cài thêm pip install python-multipart
@app.post("/upload")
def upload_file(file: UploadFile):
    my_filename = os.path.join(os.getcwd(), "data", file.filename)
    with open(my_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}