"""
Simple Student Management App (FastAPI + SQLite CRUD)
=====================================================
Unit 3: Modern API Development with FastAPI
Course: MSc (IT) — Hands-On Python

This is the simplest possible student details application using FastAPI and SQLAlchemy.
Every beginner can understand every line of this file!

CRUD Breakdown:
---------------
1. CREATE : Add a new student      ➔ db.add() + db.commit()
2. READ   : View all students      ➔ db.query(Student).all()
3. UPDATE : Toggle Active/Inactive ➔ student.is_active = not student.is_active + db.commit()
4. DELETE : Remove a student       ➔ db.delete() + db.commit()

FastAPI Superpowers:
--------------------
- Automatic Interactive API Documentation at: http://127.0.0.1:8000/docs (Swagger UI)
- Alternative Interactive Documentation at:   http://127.0.0.1:8000/redoc (ReDoc)
- Automatic Data Validation with Pydantic
- Dependency Injection for Clean Database Session Handling (`Depends(get_db)`)

How to Run:
-----------
1. Run this script directly:
   python app.py

   OR using uvicorn:
   uvicorn app:app --reload --port 8000

2. Open your browser:
   - Web App UI:     http://127.0.0.1:8000
   - Swagger Docs:   http://127.0.0.1:8000/docs
"""

import os
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel, ConfigDict

# ---------------------------------------------------------------------------
# 1. Database Setup (SQLite + SQLAlchemy ORM)
# ---------------------------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'students.db')}"

# connect_args={"check_same_thread": False} allows SQLite to work with FastAPI
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ---------------------------------------------------------------------------
# 2. Database Model (Table Definition)
# ---------------------------------------------------------------------------
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)   # Unique ID (1, 2, 3...)
    name = Column(String(100), nullable=False)           # Student Name
    roll_no = Column(String(50), nullable=False)         # Roll Number (e.g. IT-101)
    course = Column(String(100), nullable=False)         # Course (e.g. MSc IT)
    is_active = Column(Boolean, default=True)            # True = Active, False = Inactive

    def __repr__(self):
        return f"<Student #{self.id}: {self.name} ({self.roll_no})>"


# ---------------------------------------------------------------------------
# 3. Pydantic Schemas (Data Validation & Serialization for REST API)
# ---------------------------------------------------------------------------
class StudentBase(BaseModel):
    name: str
    roll_no: str
    course: str

class StudentCreate(StudentBase):
    """Schema for adding a new student via REST API."""
    pass

class StudentOut(StudentBase):
    """Schema returned to client in API responses."""
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


# ---------------------------------------------------------------------------
# 4. Dependency Injection: Database Session
# ---------------------------------------------------------------------------
def get_db():
    """
    Creates a new database session for each request,
    and automatically closes it after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------------------------
# 5. Database Initialization & Sample Data Seeder
# ---------------------------------------------------------------------------
def seed_sample_data():
    """Seed sample students if the database table is empty."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Student).count() == 0:
            samples = [
                Student(name="Aarav Sharma", roll_no="IT-101", course="MSc IT", is_active=True),
                Student(name="Diya Patel", roll_no="IT-102", course="MSc IT", is_active=True),
                Student(name="Rohan Verma", roll_no="CS-201", course="MSc CS", is_active=False),
            ]
            db.add_all(samples)
            db.commit()
    finally:
        db.close()


# ---------------------------------------------------------------------------
# 6. Initialize FastAPI App with Lifespan
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Ensure tables exist and seed sample data
    seed_sample_data()
    yield
    # Shutdown: Clean up if needed

app = FastAPI(
    title="Simple Student Management API",
    description="A beginner-friendly Student App showcasing CRUD operations with FastAPI, SQLAlchemy, and SQLite.",
    version="1.0.0",
    lifespan=lifespan
)

# Mount Static Files (CSS) and configure Jinja2 Templates
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# ===========================================================================
# 7. Web UI Routes (HTML Views matching Flask student_app)
# ===========================================================================

# 1. READ: Render student list in HTML page
@app.get("/", response_class=HTMLResponse, summary="Web UI - View Student Dashboard", include_in_schema=False)
def index(request: Request, db: Session = Depends(get_db)):
    # Query all students from SQLite, ordered by newest first
    students = db.query(Student).order_by(Student.id.desc()).all()
    total = len(students)
    active_count = sum(1 for s in students if s.is_active)
    # Calculate enrollment percentage for the progress bar (e.g. 67%)
    progress_percent = round((active_count / total * 100)) if total > 0 else 0

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "students": students,
            "total": total,
            "active_count": active_count,
            "progress_percent": progress_percent,
        }
    )


# 2. CREATE: Add a new student from HTML form
@app.post("/add", summary="Web UI - Add Student via Form", include_in_schema=False)
def add_student(
    name: str = Form(""),
    roll_no: str = Form(""),
    course: str = Form(""),
    db: Session = Depends(get_db)
):
    name = name.strip()
    roll_no = roll_no.strip()
    course = course.strip()

    # Only add if user filled in all fields
    if name and roll_no and course:
        new_student = Student(name=name, roll_no=roll_no, course=course)
        db.add(new_student)    # Stage into session
        db.commit()            # Save to SQLite database!

    # HTTP 303 SEE OTHER redirects browser to GET /
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


# 3. UPDATE: Toggle student Active / Inactive
@app.get("/toggle/{id}", summary="Web UI - Toggle Student Active Status", include_in_schema=False)
def toggle_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()
    if student:
        student.is_active = not student.is_active  # Toggle True <-> False
        db.commit()                                # Save the change!

    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


# 4. DELETE: Remove a student
@app.get("/delete/{id}", summary="Web UI - Delete Student", include_in_schema=False)
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()
    if student:
        db.delete(student)     # Mark for deletion
        db.commit()            # Save the change!

    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


# ===========================================================================
# 8. REST API Endpoints (JSON + Auto-documented in Swagger UI at /docs)
# ===========================================================================

@app.get(
    "/api/students",
    response_model=List[StudentOut],
    tags=["Students REST API"],
    summary="List all students"
)
def api_get_students(db: Session = Depends(get_db)):
    """Retrieve all student records from the SQLite database."""
    return db.query(Student).order_by(Student.id.desc()).all()


@app.post(
    "/api/students",
    response_model=StudentOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Students REST API"],
    summary="Create a new student"
)
def api_create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """Add a new student using JSON payload validated by Pydantic."""
    db_student = Student(
        name=student.name.strip(),
        roll_no=student.roll_no.strip(),
        course=student.course.strip()
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get(
    "/api/students/{id}",
    response_model=StudentOut,
    tags=["Students REST API"],
    summary="Get student by ID"
)
def api_get_student(id: int, db: Session = Depends(get_db)):
    """Fetch details of a single student by their primary key ID."""
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.patch(
    "/api/students/{id}/toggle",
    response_model=StudentOut,
    tags=["Students REST API"],
    summary="Toggle student active/inactive"
)
def api_toggle_student(id: int, db: Session = Depends(get_db)):
    """Toggle the enrollment status (Active / Inactive) of a student."""
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.is_active = not student.is_active
    db.commit()
    db.refresh(student)
    return student


@app.delete(
    "/api/students/{id}",
    status_code=status.HTTP_200_OK,
    tags=["Students REST API"],
    summary="Delete a student"
)
def api_delete_student(id: int, db: Session = Depends(get_db)):
    """Delete a student record from the SQLite database."""
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": f"Student '{student.name}' (ID: {id}) deleted successfully"}


# ---------------------------------------------------------------------------
# 9. App Entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    print("=" * 65)
    print("  🎓 Simple Student App (FastAPI) Running!")
    print("  📍 Web App UI:        http://127.0.0.1:8000")
    print("  📖 Swagger UI Docs:   http://127.0.0.1:8000/docs")
    print("  📑 ReDoc API Docs:    http://127.0.0.1:8000/redoc")
    print("=" * 65)
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
