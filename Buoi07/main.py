from fastapi import  FastAPI, HTTPException, status
import json

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

@app.get("/students")
def get_students():
    return load_students()

@app.get("/students/{id}")
def get_students(id:int):
    data = load_students()
    for student in data:
        if student["id"] == id:
            return student
    # return None
    raise HTTPException(
            status_code=404,
            detail=f"Not found {id}",
        )