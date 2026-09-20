# 📝 Simple Todo App (Flask + SQLite ORM)

> **Unit 2 — Module 03**: Database Integration with Flask  
> **Target**: Absolute Beginners (MSc IT)

This is a minimal, fully-functional web application showing all 4 **CRUD** (Create, Read, Update, Delete) database operations with Flask and SQLite.

---

## 🚀 How to Run

1. Open your terminal in this folder:
   ```bash
   cd unit-2/03_database_integration/todo_app
   ```

2. Start the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser at:  
   👉 **`http://127.0.0.1:5002`**

---

## 💡 How CRUD is Implemented in `app.py`

| Operation | Web Action | Route | SQLAlchemy Code |
|---|---|---|---|
| **C**reate | Submit task in text box | `POST /add` | `db.session.add(todo)`<br>`db.session.commit()` |
| **R**ead | View all tasks on page | `GET /` | `todos = Todo.query.all()` |
| **U**pdate | Click checkmark to toggle Done/Pending | `GET /toggle/<id>` | `todo.completed = not todo.completed`<br>`db.session.commit()` |
| **D**elete | Click trash icon 🗑️ to delete | `GET /delete/<id>` | `db.session.delete(todo)`<br>`db.session.commit()` |

---

## 🗂️ File Structure
```text
todo_app/
├── app.py              ← 80 lines of clean, commented Python backend
├── todo.db             ← SQLite database file (created automatically on first run)
├── templates/
│   └── index.html      ← Clean, single-page UI with progress bar and CRUD explanation
└── static/
    └── style.css       ← Modern, responsive stylesheet (100% offline)
```
