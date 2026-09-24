# 🎓 Simple Student App (Flask + SQLite ORM)

> **Unit 2 — Module 03**: Database Integration with Flask  
> **Target**: Absolute Beginners (MSc IT)

This is a minimal, fully-functional web application showing all 4 **CRUD** (Create, Read, Update, Delete) database operations with Flask and SQLite for managing student records.

---

## 🚀 How to Run

1. Open your terminal in this folder:
   ```bash
   cd unit-2/student_app
   ```

2. Start the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser at:  
   👉 **`http://127.0.0.1:5003`**

---

## 💡 How CRUD is Implemented in `app.py`

| Operation | Web Action | Route | SQLAlchemy Code |
|---|---|---|---|
| **C**reate | Submit student in form | `POST /add` | `db.session.add(student)`<br>`db.session.commit()` |
| **R**ead | View all students on page | `GET /` | `students = Student.query.all()` |
| **U**pdate | Click checkmark to toggle Active/Inactive | `GET /toggle/<id>` | `student.is_active = not student.is_active`<br>`db.session.commit()` |
| **D**elete | Click trash icon 🗑️ to delete | `GET /delete/<id>` | `db.session.delete(student)`<br>`db.session.commit()` |

---

## 🗂️ File Structure
```text
student_app/
├── app.py              ← ~90 lines of clean, commented Python backend
├── students.db         ← SQLite database file (created automatically on first run)
├── templates/
│   └── index.html      ← Clean, single-page UI with enrollment counter and CRUD explanation
└── static/
    └── style.css       ← Modern, responsive stylesheet (100% offline)
```
