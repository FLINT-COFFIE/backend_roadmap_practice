# importing FastAPI
from fastapi import FastAPI, Path
from typing import Optional

# creating an instance of FastAPI
app = FastAPI()

# added in memory student info
students = {1: {"name": "john", "age": 17, "class": "Level 400"}}


# making the api
@app.get("/")
def home():
    return {"name": "First Data"}


# making the path to return students
# getting by student id (path parameter)
@app.get("/get-student/{student_id}")
def get_student_id(
    # Put ... an elipsis to mark it as required
    student_id: int = Path(..., description="The ID of the student", gt=0, lt=3),
):
    return students[student_id]


# Query parameter
# getting by student name
@app.get("/get-by-name")
def get_student_name(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"404": "Not Found"}
