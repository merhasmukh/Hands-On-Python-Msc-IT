# 🎓 Simple Student App (FastAPI + SQLite ORM)

> **Unit 3 — Modern API Development with FastAPI**  
> **Target**: Absolute Beginners (MSc IT)  
> **Course**: Hands-On Python

This is a minimal, fully-functional web application showing all 4 **CRUD** (Create, Read, Update, Delete) database operations with **FastAPI** and **SQLite**, including a clean Web UI and auto-generated **Swagger UI** interactive documentation.

---

## 🚀 How to Run

### Option 1: Quick Run (Recommended)

1. Open your terminal in this directory:
   ```bash
   cd unit-3/student_app
   ```

2. Activate the Unit 3 virtual environment:
   ```bash
   # macOS / Linux:
   source ../.venv/bin/activate

   # Windows:
   ..\.venv\Scripts\activate
   ```

3. Start the application:
   ```bash
   python app.py
   ```

4. Open your browser:
   - 🌐 **Web Application UI**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - 📖 **Interactive Swagger UI Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - 📑 **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### Option 2: Using the Uvicorn CLI Directly

```bash
uvicorn app:app --reload --port 8000
```

---

## 💡 How CRUD is Implemented in `app.py`

### 1. Web UI Routes (HTML Dashboard)

| Operation | Web Action | Route | SQLAlchemy Code |
|---|---|---|---|
| **C**reate | Submit student in form | `POST /add` | `db.add(new_student)`<br>`db.commit()` |
| **R**ead | View all students on dashboard | `GET /` | `db.query(Student).all()` |
| **U**pdate | Click checkmark to toggle Active/Inactive | `GET /toggle/{id}` | `student.is_active = not student.is_active`<br>`db.commit()` |
| **D**elete | Click trash icon 🗑️ to delete | `GET /delete/{id}` | `db.delete(student)`<br>`db.commit()` |

---

### 2. REST API Endpoints (Interactive `/docs`)

| Method | Endpoint | Description | Request Body / Params |
|---|---|---|---|
| `GET` | `/api/students` | Get all students as JSON | — |
| `POST` | `/api/students` | Create student (Pydantic validated) | `{"name": "...", "roll_no": "...", "course": "..."}` |
| `GET` | `/api/students/{id}` | Get student details by ID | Path parameter: `id` |
| `PATCH` | `/api/students/{id}/toggle` | Toggle Active / Inactive status | Path parameter: `id` |
| `DELETE` | `/api/students/{id}` | Delete a student record | Path parameter: `id` |

---

## ⚖️ Unit 2 (Flask) vs Unit 3 (FastAPI) Comparison

| Concept | Flask (`unit-2/student_app`) | FastAPI (`unit-3/student_app`) |
|---|---|---|
| **App Instance** | `app = Flask(__name__)` | `app = FastAPI()` |
| **Dev Server** | `app.run(debug=True, port=5003)` | `uvicorn.run("app:app", reload=True, port=8000)` |
| **Form Data** | `request.form.get("name")` | `name: str = Form("")` *(with validation)* |
| **Redirects** | `redirect(url_for('index'))` | `RedirectResponse(url="/", status_code=303)` |
| **HTML Templates** | `render_template('index.html', ...)` | `templates.TemplateResponse(request, 'index.html', ...)` |
| **DB Session** | `db = SQLAlchemy(app)` | `SessionLocal = sessionmaker(...)` + `Depends(get_db)` |
| **Interactive Docs** | None (requires manual tools like Postman) | **Automatic at `/docs` (Swagger) & `/redoc`** |
| **Type Validation** | Manual checks | Automatic using **Pydantic** |

---

## 🗂️ File Structure

```text
student_app/
├── app.py              ← Clean, beginner-friendly FastAPI backend (Web UI + REST API)
├── requirements.txt    ← Lightweight dependencies list for this app
├── students.db         ← SQLite database file (created automatically on first run)
├── templates/
│   └── index.html      ← Responsive UI with enrollment counter, forms, and CRUD guide
└── static/
    └── style.css       ← Clean, modern, responsive CSS styling (100% offline)
```
