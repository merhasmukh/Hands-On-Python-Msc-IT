# Hands-On Python for MSc (IT)

Welcome to the comprehensive, hands-on repository for the MSc (IT) Python course! This curriculum takes students from the absolute basics of Python programming all the way to professional deployment of modern, containerized AI/Web APIs.

Below is the complete syllabus. Click on any unit title to navigate to its folder, which contains Jupyter Notebooks, executable sample code, and exercises for each topic.

---

## [Unit 1: Python Programming Foundations and Object-Oriented Programming](./unit-1)

- **Introduction to Python**: History, Features, Applications in Industry, Installing Python and VS Code, Interactive Mode vs Script Mode, Comments and Documentation.
- **Programming Constructs**: Variables and Constants, Data Types, Type Casting, Input and Output, String Formatting (f-strings), Operators, Expressions.
- **Flow of Control**: Decision Making statements: if, if-else, nested if, elif; Loop statements: for, while; break, continue, pass; enumerate, zip, range.
- **Built-in Data Structures**: Strings, Lists, Tuples, Sets, Dictionaries, List / Dictionary / Set Comprehensions.
- **Functions**: User-Defined Functions, Parameters and Return Values, `*args` and `**kwargs`, Variable Scope, Recursion, Lambda Functions, map and filter, Introduction to Decorators, Generators and Iterators.
- **Modules and Exception Handling**: Creating and Importing Modules, Standard Library Overview; Exception Handling: try, except, finally, raise, User-Defined Exceptions; Type Hints and Annotations.
- **File Handling**: Text Files, Context Managers (`with` statement), CSV Files, JSON Files.
- **Object-Oriented Programming**: Classes and Objects, Constructors (`__init__`), Instance and Class Attributes, Encapsulation, Inheritance, Polymorphism, Dunder Methods (`__str__`, `__repr__`).
- **Environment and Tooling**: pip, Virtual Environments (venv), requirements.txt.
- **Problem Solving**: Pattern Programs, Searching Techniques, Sorting Techniques.

---

## [Unit 2: Web Application Development with Flask and Databases](./unit-2)

- **Database Fundamentals**: DBMS Concepts, SQLite, MySQL, CRUD Operations, Basic SQL.
- **Flask Framework**: Introduction to Python Web Frameworks and Their Applications, Installation and Project Structure, Routing, Dynamic Routes, Templates using Jinja2, Forms and Request Handling, Blueprints.
- **Database Integration**: SQLite with Flask, MySQL with Flask, Introduction to ORM (SQLAlchemy Basics).
- **Session and File Management**: Cookies, Sessions, File Uploading, Error Handling, Custom Error Pages.
- **REST API Fundamentals**: JSON, HTTP Methods: GET, POST, PUT, DELETE; Status Codes, Building a REST API in Flask, Testing with Postman Client.

---

## [Unit 3: Modern API Development with FastAPI](./unit-3)

- **Introduction to FastAPI**: Comparison with Flask, Synchronous vs Asynchronous, Performance, Installation, Uvicorn, Project Structure.
- **Building APIs**: Path Parameters, Query Parameters, Request Bodies, Pydantic Models, Type Hints for Validation, Response Models, Status Codes.
- **Automatic Documentation**: Interactive Swagger UI, ReDoc, OpenAPI Specification.
- **Asynchronous Programming**: `async` and `await`, Async Endpoints, When to Use Async.
- **Data Layer**: Database Integration with SQLAlchemy, CRUD Service Layer, Dependency Injection (`Depends`).
- **Security and Middleware**: Authentication: JWT and OAuth2 Basics; CORS, Middleware, Request Lifecycle.
- **Testing and Quality**: Testing with pytest and FastAPI TestClient, Structuring an API Project for Maintainability, Applied Mini-Project (optionally serving a simple AI model).

---

## [Unit 4: Professional Development, Deployment and DevOps](./unit-4)

- **Project Organization**: Folder Structure, Configuration Files, Environment Variables, `.env` and `python-dotenv`, Secrets Handling, Twelve-Factor App Principles.
- **Version Control**: Git Basics, GitHub, Branching, Pull Requests, Collaboration, `.gitignore` and Commit Hygiene.
- **Linux Essentials**: File System Commands, Permissions, Process Management.
- **Deployment Fundamentals**: WSGI vs ASGI, Gunicorn, Uvicorn / Gunicorn Workers, Nginx Basics, Reverse Proxy, Domain Configuration, HTTPS and SSL, Logging and Monitoring.
- **Containerization**: Introduction to Docker, Images and Containers, Dockerizing Flask and FastAPI Applications, Docker Compose (app + database).
- **CI/CD (Introductory)**: Automated Testing and Deployment with GitHub Actions.
- **AI-Assisted Development**: Prompt Engineering Basics, Using AI Tools (ChatGPT, Copilot, Gemini) for Debugging, Documentation and Testing, Responsible and Ethical Use of AI.
- **Capstone Project**: Development and Deployment of a Database-Driven Web Application / REST API — a FastAPI backend (with a simple frontend as client), containerized, deployed behind Nginx with HTTPS, and version-controlled with a CI pipeline.