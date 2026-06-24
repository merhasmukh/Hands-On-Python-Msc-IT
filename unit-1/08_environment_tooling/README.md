# Environment and Tooling for Python Projects

> **MSc (IT) — Unit 1, Section 08**  
> Essential developer practices: virtual environments, package management, and code quality tools.

---

## 📦 pip — Python Package Installer

`pip` is the standard tool for installing Python packages from [PyPI](https://pypi.org).

### Common pip Commands

```bash
# Check pip version
pip --version

# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Install multiple packages
pip install numpy pandas matplotlib

# List installed packages
pip list

# Show info about a package
pip show requests

# Uninstall a package
pip uninstall requests

# Upgrade a package
pip install --upgrade requests

# Search for packages (deprecated on PyPI, use website)
# Visit: https://pypi.org/search/
```

---

## 🌍 Virtual Environments (venv)

A **virtual environment** is an isolated Python environment for each project. It prevents package conflicts between projects.

### Why Use Virtual Environments?

| Without venv | With venv |
|---|---|
| All packages installed globally | Packages isolated per project |
| Version conflicts between projects | Clean, reproducible environment |
| "It works on my machine" | Consistent for all team members |

### Creating and Using a Virtual Environment

```bash
# Step 1: Create the virtual environment
python -m venv .venv

# Step 2: Activate it
# macOS / Linux:
source .venv/bin/activate

# Windows (Command Prompt):
.venv\Scripts\activate.bat

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Step 3: Verify activation (you'll see (.venv) in prompt)
which python     # macOS/Linux
where python     # Windows

# Step 4: Install packages (now isolated to this project)
pip install requests numpy pandas

# Step 5: Deactivate when done
deactivate
```

> 💡 **Best Practice**: Always add `.venv/` to your `.gitignore` — never commit virtual environments!

---

## 📋 requirements.txt

A `requirements.txt` file lists all project dependencies so others can reproduce your environment.

### Generate requirements.txt

```bash
# Save current environment's packages
pip freeze > requirements.txt

# Install from requirements.txt (on another machine or fresh venv)
pip install -r requirements.txt
```

### Sample requirements.txt

See the `requirements.txt` file in this folder.

### Pinned vs Unpinned

```
# Pinned (exact version) — recommended for reproducibility
requests==2.31.0
numpy==1.26.0

# Unpinned (any compatible version)
requests
numpy

# Minimum version
requests>=2.28.0

# Compatible release
requests~=2.31.0
```

---

## 🎨 Code Formatting: Black

**Black** is an opinionated Python code formatter — it reformats your code automatically to a consistent style.

```bash
# Install Black
pip install black

# Format a single file
black hello.py

# Format entire project
black .

# Check what would change (without actually changing)
black --check .

# Show the diff
black --diff hello.py
```

### Before Black:
```python
x = {'a':   1, 'b':2}
def foo(  x,y  ):
    if x==1 :
        return y
```

### After Black:
```python
x = {"a": 1, "b": 2}


def foo(x, y):
    if x == 1:
        return y
```

---

## ⚡ Linting: Ruff

**Ruff** is an extremely fast Python linter (replaces Flake8, isort, and more). It catches errors and enforces style.

```bash
# Install Ruff
pip install ruff

# Lint a file
ruff check hello.py

# Lint the entire project
ruff check .

# Auto-fix fixable issues
ruff check --fix .

# Format with Ruff (alternative to Black)
ruff format .
```

### Common Ruff Error Codes

| Code | Meaning |
|------|---------|
| `E501` | Line too long |
| `F401` | Unused import |
| `F841` | Local variable assigned but never used |
| `E302` | Expected 2 blank lines |
| `W291` | Trailing whitespace |

### ruff.toml Configuration

```toml
# ruff.toml
line-length = 88
target-version = "py311"

[lint]
select = ["E", "F", "W", "I"]
ignore = ["E501"]
```

---

## ⚙️ VS Code Integration

### Recommended VS Code Settings (.vscode/settings.json)

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
    }
}
```

### Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| Python (Microsoft) | Core Python support |
| Pylance | IntelliSense, type checking |
| Black Formatter | Auto-format on save |
| Ruff | Fast linting |
| Jupyter | Notebook support |

---

## 🏋️ Exercises

1. Create a new folder `my_project/`, set up a virtual environment inside it
2. Install `requests` and `rich` in the virtual environment
3. Generate a `requirements.txt` for the environment
4. Install Black and format the `hello_world.py` file from section 01
5. Install Ruff and lint the `mymodule.py` from section 05; fix any issues found

---

*Previous: [07 — OOP](../07_oop/) | Next: [09 — Problem Solving](../09_problem_solving/)*
