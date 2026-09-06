# importing FastAPI
from fastapi import FastAPI, Path

# creating an instance of FastAPI
app = FastAPI()

# added in memory student info
students = {1: {"name": "john", "age": 17, "class": "Level 400"}}


# making the api
@app.get("/")
def home():
    return {"name": "First Data"}


# making the path to return students
@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(..., description="The ID of the student", gt=0, lt=3),
):
    return students[student_id]
