# Getting Started with Python

## 📖 What is Python?

Python is a **high-level, interpreted, general-purpose programming language** created by **Guido van Rossum** in **1991**.

### Key Features
- **Easy to read and write** — close to plain English
- **Interpreted** — code runs line by line (no compile step)
- **Dynamically typed** — no need to declare variable types
- **Huge standard library** — "batteries included"
- **Cross-platform** — runs on Windows, macOS, Linux

### Where Python is Used
| Industry | Application |
|----------|-------------|
| Data Science / AI | NumPy, Pandas, TensorFlow, PyTorch |
| Web Development | Django, Flask, FastAPI |
| Automation | Scripts, Selenium, Ansible |
| Cybersecurity | Penetration testing, scripting |
| Finance | Algorithmic trading, quant analysis |
| Scientific Research | SciPy, Matplotlib |

---

## ⚙️ Installation

### Step 1: Install Python 3.11+
1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest **Python 3.11+** installer for your OS
3. ✅ **Check "Add Python to PATH"** during installation (Windows)
4. Verify: open terminal and run `python --version`

### Step 2: Install VS Code
1. Download from [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Install the **Python extension** by Microsoft
3. Install the **Jupyter extension** by Microsoft

### Step 3: Set Up a Virtual Environment
```bash
# Create a virtual environment
python -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Install Jupyter
pip install jupyter jupyterlab
```

---

## 🖥️ Interactive Mode (REPL) vs Script Mode

### Interactive Mode (REPL)
- REPL = **R**ead **E**valuate **P**rint **L**oop
- Open terminal → type `python` → interactive shell starts
- Great for quick experiments

```python
>>> 2 + 3
5
>>> name = "Python"
>>> print(f"Hello, {name}!")
Hello, Python!
```

### Script Mode
- Write code in a `.py` file and run it
```bash
python hello_world.py
```

---

## 💻 hello_world.py — Your First Python Program

See `hello_world.py` in this folder.

---

## 📝 Comments and Documentation

```python
# This is a single-line comment

"""
This is a multi-line string often used as
a docstring to document a function or module.
"""

def greet(name):
    """
    Returns a greeting string.
    
    Args:
        name (str): The person's name.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"
```

---

## 🔍 Basic Debugging in VS Code

1. Set a **breakpoint** by clicking the red dot next to a line number
2. Press **F5** to start debugging
3. Use the Debug Console to inspect variables
4. Step through code with **F10** (step over) and **F11** (step into)

---

## 🏋️ Try it Yourself

1. Open terminal and type `python` — explore the REPL
2. Try: `2 ** 10`, `"hello".upper()`, `len("Python")`
3. Create a file `my_first.py` with your name and run it
4. Add a docstring to a function you write

---

*Next: [02 — Core Programming](../02_core_programming/)*
