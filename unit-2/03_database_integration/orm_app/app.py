"""
Student & Department Management Portal (Flask-SQLAlchemy ORM)
============================================================
Unit 2: Web Application Development with Flask and Databases
Course: MSc (IT) — Hands-On Python

Key Concepts Taught:
--------------------
1. Declarative Models (db.Model, Column, Integer, String, Float, DateTime)
2. Primary Keys & Unique Constraints
3. Relational Database Design: One-to-Many (1:N) Foreign Keys & Relationships
4. Complete CRUD Operations (Create, Read, Update, Delete)
5. Session Management: db.session.add(), db.session.commit(), db.session.delete()
6. Form Integration, Input Validation & Flash Messaging
7. Search & Query Filtering (LIKE / ilike, filter_by, join)

How to Run:
-----------
1. Navigate to this directory:
   cd unit-2/03_database_integration/orm_app
2. Run the application:
   python app.py
3. Open your browser:
   http://127.0.0.1:5001
"""

import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# ---------------------------------------------------------------------------
# Database Configuration
# ---------------------------------------------------------------------------
# Locate the current directory reliably across macOS, Linux, and Windows
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure SQLite database URI
# Format: sqlite:///path/to/database.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'students.db')

# Disable modification tracking to save memory and eliminate warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key required for Flask session & flash messaging
app.config['SECRET_KEY'] = 'mscit-unit2-database-integration-secret'

# Bind SQLAlchemy ORM to our Flask app
db = SQLAlchemy(app)


# ---------------------------------------------------------------------------
# Database Models (Relational Schema: Department 1 --- N Student)
# ---------------------------------------------------------------------------

class Department(db.Model):
    """
    Parent Model: Academic Department
    One department can have multiple students (1:N relationship).
    """
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)

    # 1:N Relationship: One Department has many Students
    # 'backref' adds a virtual .department property to each Student instance
    # 'cascade' ensures child students are handled if a department is deleted
    students = db.relationship('Student', backref='department', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Department {self.code}: {self.name}>"


class Student(db.Model):
    """
    Child Model: Student
    Belongs to one Department via the department_id Foreign Key.
    """
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    course = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(5), nullable=True)     # e.g., 'A+', 'A', 'B'
    gpa = db.Column(db.Float, nullable=True)           # e.g., 3.85
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Key linking this student to a department
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    def __repr__(self):
        return f"<Student #{self.id} {self.name} ({self.course})>"


# ---------------------------------------------------------------------------
# Sample Data Seeder (Helper for Beginner Students & Classroom Demos)
# ---------------------------------------------------------------------------
def seed_initial_data():
    """Populates initial departments and students if database is empty."""
    if Department.query.count() == 0:
        print("🌱 Seeding initial academic departments and students...")
        it_dept = Department(name="Information Technology", code="IT")
        cs_dept = Department(name="Computer Science", code="CS")
        ds_dept = Department(name="Data Science & AI", code="DS")

        db.session.add_all([it_dept, cs_dept, ds_dept])
        db.session.commit()

        # Seed initial students
        sample_students = [
            Student(name="Aarav Sharma", email="aarav@university.edu", course="MSc IT — Cloud Computing", 
                    grade="A+", gpa=3.85, department=it_dept),
            Student(name="Diya Patel", email="diya@university.edu", course="MSc IT — Web Systems", 
                    grade="A+", gpa=3.92, department=it_dept),
            Student(name="Rohan Verma", email="rohan@university.edu", course="MSc CS — Distributed Systems", 
                    grade="B+", gpa=3.35, department=cs_dept),
            Student(name="Ananya Iyer", email="ananya@university.edu", course="MSc DS — Machine Learning", 
                    grade="A", gpa=3.78, department=ds_dept)
        ]
        db.session.add_all(sample_students)
        db.session.commit()
        print("✅ Demo data seeded successfully!")


# ---------------------------------------------------------------------------
# Routes & Controller Logic (Full CRUD Implementation)
# ---------------------------------------------------------------------------

# 1. READ: Dashboard with Search & Filter
@app.route('/')
def index():
    """
    Renders student roster with optional search and department filtering.
    Demonstrates: Model.query, filter(), aggregations (avg, count).
    """
    search_query = request.args.get('search', '').strip()
    selected_dept = request.args.get('dept', '').strip()

    # Start with base query
    query = Student.query

    # Apply search filter if student entered a query
    if search_query:
        search_pattern = f"%{search_query}%"
        query = query.filter(
            (Student.name.ilike(search_pattern)) | 
            (Student.course.ilike(search_pattern))
        )

    # Apply department filter if selected
    if selected_dept and selected_dept.isdigit():
        query = query.filter_by(department_id=int(selected_dept))

    students = query.order_by(Student.id.desc()).all()
    departments = Department.query.order_by(Department.name).all()

    # Calculate summary metrics using SQLAlchemy aggregation
    total_students = Student.query.count()
    total_departments = Department.query.count()
    avg_gpa = db.session.query(db.func.avg(Student.gpa)).scalar() or 0.0
    honors_count = Student.query.filter(Student.gpa >= 3.7).count()

    return render_template(
        'index.html',
        students=students,
        departments=departments,
        total_students=total_students,
        total_departments=total_departments,
        avg_gpa=avg_gpa,
        honors_count=honors_count,
        search_query=search_query,
        selected_dept=selected_dept
    )


# 2. CREATE: Add New Student
@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    """
    GET: Render new student form.
    POST: Extract data, validate, instantiate Student model, commit to DB.
    """
    departments = Department.query.order_by(Department.name).all()

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        dept_id = request.form.get('department_id')
        course = request.form.get('course', '').strip()
        gpa_str = request.form.get('gpa', '').strip()
        grade = request.form.get('grade', '').strip().upper()

        # Basic Validation
        if not name or not email or not course or not dept_id:
            flash("Please complete all required fields (*).", "danger")
            return render_template('student_form.html', title="Add Student", departments=departments)

        # Check for duplicate email
        existing_student = Student.query.filter_by(email=email).first()
        if existing_student:
            flash(f"A student with email '{email}' already exists!", "danger")
            return render_template('student_form.html', title="Add Student", departments=departments)

        # Convert GPA to float safely
        gpa = None
        if gpa_str:
            try:
                gpa = float(gpa_str)
            except ValueError:
                gpa = None

        # Create new ORM object and save to database
        new_student = Student(
            name=name,
            email=email,
            course=course,
            department_id=int(dept_id),
            gpa=gpa,
            grade=grade
        )
        db.session.add(new_student)
        db.session.commit()

        flash(f"Student '{name}' added successfully to the database!", "success")
        return redirect(url_for('index'))

    return render_template('student_form.html', title="Add New Student", departments=departments, student=None)


# 3. UPDATE: Edit Existing Student
@app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    """
    GET: Retrieve student by primary key and display form pre-filled.
    POST: Update attributes and commit transaction.
    """
    # Modern SQLAlchemy 2.0+ pattern: db.session.get(Model, id)
    student = db.session.get(Student, id)
    if not student:
        flash(f"Student with ID #{id} was not found.", "danger")
        return redirect(url_for('index'))

    departments = Department.query.order_by(Department.name).all()

    if request.method == 'POST':
        student.name = request.form.get('name', '').strip()
        new_email = request.form.get('email', '').strip().lower()
        student.course = request.form.get('course', '').strip()
        dept_id = request.form.get('department_id')
        student.grade = request.form.get('grade', '').strip().upper()
        
        gpa_str = request.form.get('gpa', '').strip()
        student.gpa = float(gpa_str) if gpa_str else None

        # Check for email collision with other students
        email_owner = Student.query.filter_by(email=new_email).first()
        if email_owner and email_owner.id != student.id:
            flash(f"Email '{new_email}' is already used by another student!", "danger")
            return render_template('student_form.html', title="Edit Student", departments=departments, student=student)

        student.email = new_email
        if dept_id and dept_id.isdigit():
            student.department_id = int(dept_id)

        # Commit modified attributes
        db.session.commit()
        flash(f"Student record for '{student.name}' updated successfully!", "success")
        return redirect(url_for('index'))

    return render_template('student_form.html', title="Edit Student Record", departments=departments, student=student)


# 4. DELETE: Remove Student
@app.route('/students/<int:id>/delete', methods=['POST'])
def delete_student(id):
    """
    POST: Deletes the specified student record from the database.
    Demonstrates: db.session.delete() and db.session.commit().
    """
    student = db.session.get(Student, id)
    if student:
        student_name = student.name
        db.session.delete(student)
        db.session.commit()
        flash(f"Student '{student_name}' (ID #{id}) has been deleted.", "success")
    else:
        flash(f"Student ID #{id} not found.", "danger")

    return redirect(url_for('index'))


# 5. Department Management Route (Demonstrates 1:N Parent management)
@app.route('/departments', methods=['GET', 'POST'])
def departments():
    """
    GET: List all departments with student count.
    POST: Create a new department.
    """
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        code = request.form.get('code', '').strip().upper()

        if not name or not code:
            flash("Department name and code are required.", "danger")
        elif Department.query.filter((Department.name == name) | (Department.code == code)).first():
            flash(f"Department with name '{name}' or code '{code}' already exists.", "danger")
        else:
            new_dept = Department(name=name, code=code)
            db.session.add(new_dept)
            db.session.commit()
            flash(f"Department '{name} ({code})' created successfully!", "success")
            return redirect(url_for('departments'))

    all_departments = Department.query.order_by(Department.name).all()
    return render_template('departments.html', departments=all_departments)


# 6. Manual Demo Data Seeder Route
@app.route('/seed')
def seed_data():
    """Convenience route to populate sample data for classroom demonstration."""
    seed_initial_data()
    flash("Demo academic data successfully verified/seeded!", "success")
    return redirect(url_for('index'))


# ---------------------------------------------------------------------------
# Application Entrypoint
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Ensure database tables exist within the Flask application context
    with app.app_context():
        db.create_all()
        seed_initial_data()

    print("=" * 70)
    print("  🎓 EduPortal Student ORM Web Application Running!")
    print("  📍 Local URL: http://127.0.0.1:5001")
    print("  💡 Features : Full CRUD, SQLite ORM, 1:N Relationships, Search")
    print("=" * 70)
    app.run(debug=True, port=5001)
