# Unit II — Web Application Development with Flask and Databases

> **Course**: MSc (IT) — Hands-On Python  
> **Target**: Semester Students (Beginners to Intermediate)  
> **Python Version**: 3.11+

---

## 📚 What You Will Learn

By the end of this unit, you will be able to:

- Understand core Database Management System (DBMS) concepts.
- Write raw SQL to perform CRUD operations in SQLite and MySQL.
- Build dynamic web applications using the Flask framework.
- Use Jinja2 templates, handle forms, and structure projects with Blueprints.
- Integrate databases with Flask natively and via SQLAlchemy (ORM).
- Manage application state (Cookies, Sessions), handle file uploads, and create custom error pages.
- Design and expose basic REST APIs using Flask and test them with Postman.

---

## 🗂️ Folder Structure

```
unit-2/
├── README.md                        ← You are here
├── requirements.txt                 ← Dependencies
├── 01_database_fundamentals/        ← DBMS concepts, SQLite, basic SQL, CRUD
├── 02_flask_framework/              ← Flask intro, routing, templates, forms
├── 03_database_integration/         ← Flask with SQLite/MySQL, SQLAlchemy ORM
├── 04_state_files_errors/           ← Cookies, sessions, uploads, error handling
└── 05_rest_api/                     ← JSON, HTTP methods, Flask REST API, Postman
```

---

## 🚀 How to Use These Materials

### For Students

1. **Set up your environment** using the instructions below.
2. Open each sub-directory in order.
3. Read through the `.ipynb` notebooks in **Jupyter Lab** or **VS Code**.
4. Run the demo applications located inside each module (e.g., `python app.py`).
5. Complete the **Exercise** files (`.py` scripts) provided in the `exercises/` folders.

### For the Professor

- **Notebooks**: Use these as your primary lecture materials. They mix theory, diagrams (via markdown), and executable code.
- **Demo Apps**: Run these standalone apps to demonstrate concepts like forms, sessions, or file uploads live in the browser.
- **Exercises**: Use these for lab sessions or graded assignments.

---

## ⚙️ Prerequisites & Setup

```bash
# 1. Navigate to the unit-2 folder
cd unit-2

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
# macOS / Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 4. Install required packages
pip install -r requirements.txt
```

---

## 📋 Topic Overview

| # | Topic | Focus |
|---|-------|-------|
| 01 | Database Fundamentals | Tables, Primary Keys, CRUD, `sqlite3` |
| 02 | Flask Framework | `@app.route`, Jinja2 (`{{ }}`), HTTP Methods, Blueprints |
| 03 | Database Integration | Flask-SQLAlchemy, Models, Migrations |
| 04 | State, Files & Errors | `session`, `request.files`, `@app.errorhandler` |
| 05 | REST API | JSON responses, `jsonify`, API endpoints, Postman |

---

*Made with ❤️ for MSc (IT) students — Python 3.11+*
