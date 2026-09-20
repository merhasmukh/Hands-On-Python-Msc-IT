"""
Simple Todo App (Flask + SQLite CRUD)
=====================================
Unit 2: Web Application Development with Flask & Databases
Course: MSc (IT) — Hands-On Python

This is the simplest possible CRUD application using Flask and Flask-SQLAlchemy.
Every beginner can understand every line of this file!

CRUD Breakdown:
---------------
1. CREATE : Add a new task      ➔ db.session.add() + db.session.commit()
2. READ   : View all tasks      ➔ Todo.query.all()
3. UPDATE : Mark task as done   ➔ todo.completed = not todo.completed + db.session.commit()
4. DELETE : Remove a task       ➔ db.session.delete() + db.session.commit()

How to Run:
-----------
1. Run this script:
   python app.py
2. Open your browser:
   http://127.0.0.1:5002
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# 1. Initialize Flask App
app = Flask(__name__)

# 2. Configure SQLite Database (saved in the same folder as app.py)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Initialize SQLAlchemy
db = SQLAlchemy(app)


# ---------------------------------------------------------------------------
# Database Model (Table)
# ---------------------------------------------------------------------------
class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)         # Unique ID (1, 2, 3...)
    title = db.Column(db.String(200), nullable=False)     # Task description
    completed = db.Column(db.Boolean, default=False)     # True = Done, False = Pending

    def __repr__(self):
        return f"<Todo #{self.id}: {self.title} (Done: {self.completed})>"


# ---------------------------------------------------------------------------
# Routes (CRUD Operations)
# ---------------------------------------------------------------------------

# 1. READ: Show all tasks and the add form
@app.route('/')
def index():
    # Query all todos from SQLite, ordered by newest first
    todos = Todo.query.order_by(Todo.id.desc()).all()
    total = len(todos)
    done_count = sum(1 for t in todos if t.completed)
    progress = round((done_count / total * 100)) if total > 0 else 0
    return render_template('index.html', todos=todos, total=total, done_count=done_count, progress=progress)


# 2. CREATE: Add a new task from the form
@app.route('/add', methods=['POST'])
def add_todo():
    # Get the text entered by user in the input box
    title = request.form.get('title', '').strip()

    # Only add if user didn't submit empty text
    if title:
        new_todo = Todo(title=title)
        db.session.add(new_todo)     # Stage into session
        db.session.commit()          # Save to SQLite database!

    return redirect(url_for('index'))


# 3. UPDATE: Toggle task between Done and Pending
@app.route('/toggle/<int:id>')
def toggle_todo(id):
    # Find the task by its ID
    todo = db.session.get(Todo, id)
    if todo:
        todo.completed = not todo.completed   # Toggle True <-> False
        db.session.commit()                  # Save the change!

    return redirect(url_for('index'))


# 4. DELETE: Remove a task
@app.route('/delete/<int:id>')
def delete_todo(id):
    # Find the task by its ID
    todo = db.session.get(Todo, id)
    if todo:
        db.session.delete(todo)      # Mark for deletion
        db.session.commit()          # Save the change!

    return redirect(url_for('index'))


# ---------------------------------------------------------------------------
# App Entrypoint
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Create tables if they do not exist yet
    with app.app_context():
        db.create_all()

    print("=" * 60)
    print("  📝 Simple Todo App Running!")
    print("  📍 Open in Browser: http://127.0.0.1:5002")
    print("=" * 60)
    app.run(debug=True, port=5002)
