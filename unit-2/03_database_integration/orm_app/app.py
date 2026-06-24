from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite Database
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------------------------------------------------
# Define the Model
# ---------------------------------------------------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(2))

    def __repr__(self):
        return f'<Student {self.name}>'

# ---------------------------------------------------------
# Create the Database Tables
# ---------------------------------------------------------
with app.app_context():
    db.create_all()

# ---------------------------------------------------------
# Routes (CRUD Operations)
# ---------------------------------------------------------

@app.route('/')
def index():
    return "Welcome to the Student ORM App! Visit /students to view data."

# CREATE
@app.route('/students/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    course = request.form.get('course')
    grade = request.form.get('grade')
    
    if not name or not course:
        return "Missing data", 400
        
    new_student = Student(name=name, course=course, grade=grade)
    db.session.add(new_student)
    db.session.commit()
    
    return f"Student {name} added successfully!"

# READ
@app.route('/students')
def get_students():
    students = Student.query.all()
    # In a real app, you would pass this to a template
    result = ""
    for s in students:
        result += f"ID: {s.id} | Name: {s.name} | Course: {s.course} | Grade: {s.grade}<br>"
    return result if result else "No students found."

if __name__ == '__main__':
    app.run(debug=True, port=5001)
