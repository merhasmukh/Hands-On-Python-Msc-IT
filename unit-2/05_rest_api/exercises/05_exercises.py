"""
05_exercises.py — REST API Fundamentals
=======================================
MSc (IT) — Unit 2: Web Application Development with Flask and Databases

Instructions:
- Below is an empty Flask app.
- Write endpoints to manage a list of "students".
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "course": "Python"},
    {"id": 2, "name": "Bob", "course": "Java"}
]

# ===========================================================================
# Exercise 1: GET All Students
# ===========================================================================
"""
Write a route `/api/students` (GET) that returns the list of students in JSON format.
"""
@app.route('/api/students', methods=['GET'])
def get_all_students():
    # Write your code here:
    pass

# ===========================================================================
# Exercise 2: GET Single Student
# ===========================================================================
"""
Write a route `/api/students/<int:student_id>` (GET) that returns a single 
student if found, or a 404 error with a message if not found.
"""
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # Write your code here:
    pass

# ===========================================================================
# Exercise 3: POST New Student
# ===========================================================================
"""
Write a route `/api/students` (POST) that accepts JSON data (name and course),
creates a new student with a unique ID, appends it to the list, and returns
the new student with a 201 status code.
"""
@app.route('/api/students', methods=['POST'])
def add_student():
    # Write your code here:
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("  Starting REST API Server for Exercises...")
    print("  Check http://127.0.0.1:5000/api/students")
    print("=" * 60)
    app.run(debug=True)
