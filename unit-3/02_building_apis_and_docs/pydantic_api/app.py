from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Management API")

# 1. Define our Pydantic Model (Schema)
class Student(BaseModel):
    name: str
    age: int
    course: str
    is_active: bool = True  # Default value

# In-memory database
students_db = {
    1: {"name": "Alice", "age": 22, "course": "Python", "is_active": True}
}

# GET with Path Parameter
@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# POST with Request Body (Pydantic Model)
@app.post("/students/", status_code=201)
def create_student(student: Student):
    # 'student' is automatically validated!
    new_id = max(students_db.keys()) + 1 if students_db else 1
    # Convert Pydantic object to dictionary
    students_db[new_id] = student.model_dump()
    
    return {"message": "Student created successfully", "id": new_id, "student": student}

# GET with Query Parameters
@app.get("/students/")
def list_students(skip: int = 0, limit: int = 10):
    # Convert dict values to a list and apply skip/limit
    students_list = list(students_db.values())
    return students_list[skip : skip + limit]

# Run with: uvicorn app:app --reload
# View Docs at: http://127.0.0.1:8000/docs
