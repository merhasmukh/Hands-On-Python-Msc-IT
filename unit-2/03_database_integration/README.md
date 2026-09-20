# Unit 2 — Module 03: Database Integration with Flask

> **Course**: MSc (IT) — Hands-On Python  
> **Level**: Beginner to Intermediate  
> **Topic**: Persistent Data Storage, Raw SQL vs. Object-Relational Mapping (ORM), Flask-SQLAlchemy, CRUD Operations, and Relational Foreign Keys.

---

## 🧭 Overview & Learning Objectives

In web development, variables stored in Python memory are destroyed whenever the server restarts. Persistent data requires an external database management system (DBMS).

In this module, students learn:
1. **The Evolution of Data Storage**: Moving from in-memory lists and raw SQL (`sqlite3`) to declarative Object-Relational Mapping (`Flask-SQLAlchemy`).
2. **The ORM Mental Model**:
   - Python Class $\leftrightarrow$ Database Table
   - Class Attribute $\leftrightarrow$ Column & Constraints (`primary_key`, `nullable`, `unique`)
   - Class Object $\leftrightarrow$ Database Row
3. **The SQLAlchemy Session Lifecycle**: Staging (`db.session.add()`), committing (`db.session.commit()`), and rolling back transactions on error (`db.session.rollback()`).
4. **Relational Schemas (1:N)**: Linking tables using `db.ForeignKey` and accessing related entities intuitively with `db.relationship()`.
5. **Full Web CRUD**: Building real-world Create, Read, Update, and Delete routes with HTML forms, search filtering, and user feedback (flash notifications).

---

## 🗂️ Module Contents

```text
03_database_integration/
├── README.md                      ← You are here
├── 03_database_integration.ipynb  ← Master guide: Direct SQLite ➔ Flask-SQLAlchemy (ORM)
├── 03_sqlite_direct_flask.ipynb   ← Companion guide: Direct SQLite in Flask without ORM
├── todo_app/                      ← [NEW] Super simple beginner Todo CRUD app (Port 5002)
│   ├── app.py                     ← 80 lines of clean, commented CRUD code
│   ├── templates/index.html       ← Single-page task dashboard & CRUD cheat-sheet
│   └── static/style.css           ← Modern, responsive, 100% offline styling
├── exercises/
│   └── 03_exercises.py            ← 4 progressive exercises with built-in test suite (--test)
└── orm_app/                       ← Relational academic portal with 1:N models (Port 5001)
    ├── app.py                     ← Flask backend with Department (1) <-> Student (N) models
    ├── templates/                 ← Jinja2 HTML templates (base, index, form, depts)
    └── static/css/style.css       ← Modern, offline-first styling (cards, tables, badges)
```

---

## 🚀 Quickstart Guide

### 1. Ultra-Simple Beginner App (`todo_app`) — Start Here!
The easiest way for absolute beginners to understand CRUD in 2 minutes:
```bash
cd todo_app
python app.py
```
Open your browser at: **`http://127.0.0.1:5002`**

**What to try:**
- ➕ Type a task and hit Enter to test **Create** (`db.session.add()`).
- 📋 See all tasks appear in real-time to test **Read** (`Todo.query.all()`).
- 🔄 Click the checkbox icon to toggle Done/Pending to test **Update** (`todo.completed = not todo.completed`).
- 🗑️ Click the trash icon to test **Delete** (`db.session.delete()`).

### 2. Standalone Academic Portal (`orm_app`)
Launch the complete Student & Department management portal with relational models:
```bash
cd orm_app
python app.py
```
Open your browser at: **`http://127.0.0.1:5001`**

**Features to Explore:**
- 📋 View all students with GPA indicator pills and department badges.
- 🔍 Search students by name or program, or filter by academic department.
- ➕ Add a new student (demonstrating foreign key selection).
- ✏️ Edit existing records.
- 🗑️ Delete students with safety confirmation.
- 🏛️ Manage academic departments and inspect enrolled student counts.
- 🌱 1-click Demo Data Seeder for classroom demonstrations.

### 3. Lab Exercises (`exercises/`)
Complete the exercises in `exercises/03_exercises.py`:
```bash
# Run the automated verification test suite:
python exercises/03_exercises.py --test

# Run the interactive API web server:
python exercises/03_exercises.py
```

---

## 🔄 Raw SQL vs. SQLAlchemy ORM Cheat-Sheet

| Operation | Raw SQL (`sqlite3`) | Flask-SQLAlchemy (ORM) |
|---|---|---|
| **Create Table** | `CREATE TABLE students (id INT PRIMARY KEY, name TEXT);` | `class Student(db.Model): id = ...` |
| **Insert Row** | `cursor.execute("INSERT INTO students VALUES (?, ?)", (1, 'Eve'))` | `db.session.add(Student(name='Eve'))`<br>`db.session.commit()` |
| **Select All** | `cursor.execute("SELECT * FROM students"); rows = cur.fetchall()` | `students = Student.query.all()` |
| **Filter by Column** | `cursor.execute("SELECT * FROM students WHERE grade=?", ('A',))` | `Student.query.filter_by(grade='A').all()` |
| **Get by Primary Key** | `cursor.execute("SELECT * FROM students WHERE id=?", (1,))` | `student = db.session.get(Student, 1)` |
| **Update Row** | `cursor.execute("UPDATE students SET grade=? WHERE id=?", ('A+', 1))` | `student.grade = 'A+'`<br>`db.session.commit()` |
| **Delete Row** | `cursor.execute("DELETE FROM students WHERE id=?", (1,))` | `db.session.delete(student)`<br>`db.session.commit()` |

---

## 🔌 Switching Database Engines (SQLite vs. MySQL)

Because SQLAlchemy is an **abstraction layer**, you can switch database backends by updating a single configuration line in `app.py`:

```python
# 1. SQLite (Default - Serverless file, zero setup)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

# 2. MySQL / MariaDB (Production client-server)
# pip install pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/school_db'

# 3. PostgreSQL (Enterprise)
# pip install psycopg2-binary
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/school_db'
```
*Zero Python model or query code needs to be modified when switching!*

---

## ⚠️ Top 5 Beginner Traps & How to Fix Them

1. **Forgetting `db.session.commit()`**:
   - *Symptom*: Adding or editing an object works in Python, but when you refresh the browser, the data vanishes.
   - *Fix*: Changes are only staged in memory until `db.session.commit()` writes them to the SQLite file.
2. **`RuntimeError: Working outside of application context`**:
   - *Symptom*: Calling `db.create_all()` at top-level crashes with context error.
   - *Fix*: Wrap database initialization in `with app.app_context(): db.create_all()`.
3. **Modifying Models after `db.create_all()`**:
   - *Symptom*: You added a new column (e.g., `phone = db.Column(...)`), but SQLite throws `OperationalError: no such column`.
   - *Fix*: `db.create_all()` only creates *missing* tables; it never alters existing tables. For development, delete `students.db` and re-run, or use Flask-Migrate in production.
4. **Using Deprecated `Model.query.get(id)`**:
   - *Symptom*: Deprecation warnings in SQLAlchemy 2.0.
   - *Fix*: Use `db.session.get(Model, id)`.
5. **Direct String Formatting in Queries**:
   - *Symptom*: `f"SELECT * FROM users WHERE name = '{name}'"` allows SQL injection attacks.
   - *Fix*: Always use ORM methods (`filter_by()`) or parameterized queries.
