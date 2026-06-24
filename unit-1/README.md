# Unit I — Python Programming Foundations and OOP

> **Course**: MSc (IT) — Hands-On Python  
> **Target**: Semester Students (Beginners to Intermediate)  
> **Python Version**: 3.11+

---

## 📚 What You Will Learn

By the end of this unit, you will be able to:

- Write modular, well-structured Python programs using control structures and data structures
- Apply object-oriented programming principles (encapsulation, inheritance, polymorphism)
- Handle files, exceptions, and external data formats (CSV, JSON)
- Use standard Python tooling: `pip`, virtual environments, linting

---

## 🗂️ Folder Structure

```
unit-1/
├── README.md                        ← You are here
├── 01_getting_started/              ← History, setup, REPL, VS Code
├── 02_core_programming/             ← Variables, operators, conditions, loops
├── 03_data_structures/              ← Strings, Lists, Tuples, Sets, Dicts
├── 04_functions/                    ← Functions, lambdas, decorators, generators
├── 05_modules_and_errors/           ← Modules, stdlib, exceptions, type hints
├── 06_file_handling/                ← Text, CSV, JSON files
├── 07_oop/                          ← Classes, OOP principles, dunder methods
├── 08_environment_tooling/          ← pip, venv, Black, Ruff
└── 09_problem_solving/              ← Patterns, searching, sorting
```

---

## 🚀 How to Use These Materials

### For Students

1. **Clone or download** this repository
2. **Set up your environment** (follow `01_getting_started/README.md`)
3. Open each notebook in **Jupyter Lab** or **VS Code** with the Jupyter extension
4. Read the explanations, **run every code cell**, and observe the output
5. Complete the **Exercise** cells at the end of each section (marked with 🏋️)

### For the Professor

- Notebooks are self-contained — open any topic directly in class
- Each notebook has:
  - 📖 **Concept explanation** with markdown
  - 💻 **Live code demos** with expected output shown in comments
  - ⚠️ **Common mistakes** section
  - 🏋️ **Exercises** at the end (students fill in)
- Use the `exercises/` `.py` files for graded assignments or lab sessions

---

## ⚙️ Prerequisites & Setup

```bash
# 1. Install Python 3.11+
# Download from: https://www.python.org/downloads/

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
# macOS / Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 4. Install required packages
pip install jupyter jupyterlab notebook

# 5. Launch Jupyter Lab
jupyter lab
```

---

## 📋 Topics at a Glance

| # | Topic | Key Concepts |
|---|-------|-------------|
| 01 | Getting Started | History, features, installation, REPL, VS Code |
| 02 | Core Programming | Variables, I/O, operators, conditionals, loops |
| 03 | Data Structures | Strings, Lists, Tuples, Sets, Dicts, Comprehensions |
| 04 | Functions | Functions, *args/**kwargs, scope, lambda, map/filter, decorators, generators |
| 05 | Modules & Errors | Modules, stdlib, exceptions, type hints |
| 06 | File Handling | Text files, CSV, JSON, context managers |
| 07 | OOP | Classes, encapsulation, inheritance, polymorphism, dunder methods |
| 08 | Environment & Tooling | pip, venv, Black, Ruff |
| 09 | Problem Solving | Patterns, searching, sorting, complexity |

---

## 📝 Notebook Conventions

| Symbol | Meaning |
|--------|---------|
| 📖 | Concept / Theory |
| 💻 | Live Code Demo |
| 💡 | Pro Tip |
| ⚠️ | Common Mistake / Watch Out |
| 🏋️ | Exercise (you must solve this) |
| ✅ | Expected Output |

---

*Made with ❤️ for MSc (IT) students — Python 3.11+*
