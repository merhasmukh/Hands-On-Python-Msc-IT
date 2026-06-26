# Unit III — Modern API Development with FastAPI

> **Course**: MSc (IT) — Hands-On Python  
> **Target**: Semester Students (Beginners to Intermediate)  
> **Python Version**: 3.11+

---

## 📚 What You Will Learn

By the end of this unit, you will be able to:

- Understand the difference between traditional synchronous frameworks (like Flask) and modern asynchronous frameworks (like FastAPI).
- Build robust APIs using **FastAPI** and **Uvicorn**.
- Utilize **Pydantic** models for automatic data validation, serialization, and type hinting.
- Use automatic interactive API documentation via **Swagger UI** and **ReDoc**.
- Write and understand asynchronous Python code (`async` and `await`).
- Integrate a database (SQLite) using **SQLAlchemy** via a structured CRUD service layer and Dependency Injection (`Depends`).
- Secure APIs using **OAuth2 Password Bearer** (JWT tokens) and handle middleware/CORS.
- Write unit tests for APIs using **Pytest** and `TestClient`.
- Structure and serve a simple Mock AI model through a REST API.

---

## 🗂️ Folder Structure

```
unit-3/
├── README.md                        ← You are here
├── requirements.txt                 ← Dependencies
├── 01_fastapi_intro/                ← Intro, Sync vs Async, Uvicorn
├── 02_building_apis_and_docs/       ← Pydantic, Validation, Swagger UI
├── 03_async_programming/            ← async/await deep dive
├── 04_data_layer/                   ← SQLAlchemy CRUD, Dependency Injection
├── 05_security_and_middleware/      ← JWT Auth, CORS, Middleware
└── 06_testing_and_project/          ← Pytest, Project Structure, AI API
```

---

## 🚀 How to Use These Materials

### For Students

1. **Set up your environment** using the instructions below.
2. Open each sub-directory in order.
3. Read through the `.ipynb` notebooks in **Jupyter Lab** or **VS Code**.
4. Run the demo applications using `uvicorn` (e.g., `uvicorn app:app --reload`).
5. Complete the **Exercise** files (`.py` scripts) provided in the `exercises/` folders.

### For the Professor

- **Notebooks**: Use these as your primary lecture materials. They mix theory, architectural diagrams, and executable code snippets.
- **Demo Apps**: Run these standalone APIs to demonstrate concepts live. The automatic Swagger UI (`/docs`) makes it incredibly easy to show students how the API works without needing a frontend or Postman.
- **Exercises**: Use these for lab sessions or graded assignments.

---

## ⚙️ Prerequisites & Setup

```bash
# 1. Navigate to the unit-3 folder
cd unit-3

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
| 01 | Intro to FastAPI | `FastAPI()`, `uvicorn`, Sync vs Async concepts |
| 02 | Building APIs & Docs | `@app.get`, Path/Query Params, Pydantic, `/docs` |
| 03 | Async Programming | `async def`, `await asyncio.sleep()`, Event Loop |
| 04 | Data Layer | `SessionLocal`, `Depends(get_db)`, SQLAlchemy |
| 05 | Security | `OAuth2PasswordBearer`, JWT, `CORSMiddleware` |
| 06 | Testing & Project | `TestClient`, `pytest`, Serving an AI model |

---

*Made with ❤️ for MSc (IT) students — Python 3.11+*
