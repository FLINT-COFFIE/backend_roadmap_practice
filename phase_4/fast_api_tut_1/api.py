# importing FastAPI
from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

# creating an instance of FastAPI
app = FastAPI()

# added in memory student info
students = {1: {"name": "john", "age": 17, "year": "Level 400"}}


# defining the shape of the data for post
class Student(BaseModel):
    name: str
    age: int
    year: str


# defining the update model
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


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
def get_student_name(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"404": "Not Found"}


# making the post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]


# making a put method
@app.put("/update-student")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]
