# 🚀 Hands-On Flask Practice Projects & Problem Statements
### Unit 2: Web Application Development with Flask & Databases
> **Target Audience:** Master of Science in Information Technology (MSc IT)  
> **Course:** Hands-On Python Web Development  
> **Objective:** Bridge theoretical classroom knowledge with real-world application by building an end-to-end CRUD web application using Flask, Jinja2 templates, forms, and persistent storage.

---

## 📋 Assignment Overview for Students

Choose **ONE** of the 6 real-world problem statements below to build your individual lab project.

### Core Deliverables:
1. **Flask Application (`app.py`)**: Well-structured routes handling HTTP `GET` and `POST` requests.
2. **HTML Templates (`templates/`)**: Clean, responsive UI using Jinja2 inheritance (`base.html`).
3. **Data Management**:
   - **Phase 1 (Module 02)**: In-memory Python lists/dictionaries with form handling.
   - **Phase 2 (Module 03)**: Persistent database tables using SQLite and Flask-SQLAlchemy.
4. **CRUD Actions**: The application must implement **Create**, **Read**, **Update**, and **Delete**.

---

## 📌 Project 1: Student Daily Expense Tracker

### 🎯 Problem Context
College students often struggle to keep track of their daily pocket money and hostel expenditures across categories like Food, Books, Stationery, and Travel. You need to build a lightweight web expense tracker.

### 🗂️ Data Schema / Model
| Field | Type | Description | Example |
|---|---|---|---|
| `id` | Integer | Primary key / Unique identifier | `1` |
| `title` | String(100) | Description of the expense | `"Canteen Lunch"` |
| `amount` | Float | Cost in Rupees/Dollars | `150.00` |
| `category` | String(50) | Expense category | `"Food"`, `"Books"`, `"Travel"`, `"Other"` |
| `date` | Date/DateTime | Date when expense occurred | `2026-09-20` |

### 🛠️ Required Routes & Functionality
- `GET /`: Dashboard showing table of all expenses, category badges, and **Total Money Spent** summary card.
- `POST /add`: Form endpoint to record a new expense with title, amount, and category dropdown.
- `GET /filter?category=Food`: Filter expenses to display only matching category items.
- `POST /delete/<id>`: Delete an incorrect or accidental expense entry.

### 🌟 Bonus Challenge (MSc IT Distinction)
Add a summary bar showing how much percentage of the total budget was spent on each category.

---

## 📌 Project 2: Personal Book Reading List

### 🎯 Problem Context
Book lovers and students often maintain lists of textbooks, research papers, and novels they want to read. You need to build a personal reading bookshelf web app.

### 🗂️ Data Schema / Model
| Field | Type | Description | Example |
|---|---|---|---|
| `id` | Integer | Primary key | `1` |
| `title` | String(150) | Title of the book | `"Atomic Habits"` |
| `author` | String(100) | Author's name | `"James Clear"` |
| `genre` | String(50) | Subject / Genre | `"Self-Help"`, `"Computer Science"` |
| `is_read` | Boolean | Reading status | `True` (Completed) / `False` (Want to Read) |
| `rating` | Integer | Optional rating | `1` to `5` stars |

### 🛠️ Required Routes & Functionality
- `GET /`: Display two sections: **Currently Reading / Want to Read** and **Completed Books**.
- `POST /add`: Form to add a new book to the library shelf.
- `GET /toggle/<id>`: One-click status button to toggle between "Want to Read" and "Completed".
- `POST /update-rating/<id>`: Submit a 1–5 star rating for finished books.
- `POST /delete/<id>`: Remove a book from the reading list.

### 🌟 Bonus Challenge (MSc IT Distinction)
Include a progress counter: `"You have completed 4 of 10 books (40%)"`.

---

## 📌 Project 3: Contact Book & Mini Phone Directory

### 🎯 Problem Context
A personal contact directory to store family, friends, and faculty contact details with instant search and favorite pinning.

### 🗂️ Data Schema / Model
| Field | Type | Description | Example |
|---|---|---|---|
| `id` | Integer | Primary key | `1` |
| `name` | String(100) | Contact's full name | `"Dr. Sunita Rao"` |
| `phone` | String(15) | Mobile phone number | `"+91 98765 43210"` |
| `email` | String(120) | Email address | `"sunita.rao@university.edu"` |
| `relation` | String(50) | Tag/Relationship | `"Faculty"`, `"Friend"`, `"Family"` |
| `is_favorite` | Boolean | Starred contact flag | `True` / `False` |

### 🛠️ Required Routes & Functionality
- `GET /`: Alphabetically sorted list of contacts with favorite contacts pinned at the top.
- `GET /search?q=name`: Search bar that filters contacts dynamically.
- `POST /contacts/add`: Form to register a new contact with phone number validation.
- `GET /contacts/favorite/<id>`: Toggle the ⭐ Favorite status.
- `POST /contacts/delete/<id>`: Delete contact with confirmation prompt.

### 🌟 Bonus Challenge (MSc IT Distinction)
Validate that the phone number contains exactly 10 digits before saving.

---

## 📌 Project 4: Campus Lost & Found Notice Board

### 🎯 Problem Context
College campuses frequently have misplaced ID cards, notebooks, flash drives, and water bottles. Build a digital notice board where students can report found items and owners can claim them.

### 🗂️ Data Schema / Model
| Field | Type | Description | Example |
|---|---|---|---|
| `id` | Integer | Primary key | `1` |
| `item_name` | String(100) | Name of the object | `"Blue Scientific Calculator"` |
| `location_found` | String(100) | Campus location | `"Computer Lab 3, Row B"` |
| `finder_name` | String(100) | Name of student who found it | `"Rohan Verma (MSc IT)"` |
| `contact_info` | String(100) | Contact details | `"rohan@student.edu / Room 204"` |
| `is_claimed` | Boolean | Resolved status | `False` (Open) / `True` (Claimed) |

### 🛠️ Required Routes & Functionality
- `GET /`: Notice board displaying open, unclaimed items as cards.
- `POST /report`: Form for any student to report a found item.
- `POST /claim/<id>`: Mark an item as "Claimed & Returned ✅" with the claimant's name.
- `GET /archive`: View historical list of items successfully returned to owners.
- `POST /delete/<id>`: Moderator route to remove expired notices.

### 🌟 Bonus Challenge (MSc IT Distinction)
Display a `"Recent"` badge on notices reported within the last 24 hours.

---

## 📌 Project 5: Movie & Web Series Watchlist

### 🎯 Problem Context
Students love watching movies and TV series across platforms like Netflix, Prime, YouTube, and Hotstar. Build a personalized watchlist to track recommendations and personal reviews.

### 🗂️ Data Schema / Model
| Field | Type | Description | Example |
|---|---|---|---|
| `id` | Integer | Primary key | `1` |
| `title` | String(120) | Movie or series name | `"Interstellar"` |
| `platform` | String(50) | Streaming service | `"Netflix"`, `"Prime"`, `"Theater"` |
| `genre` | String(50) | Category | `"Sci-Fi"`, `"Thriller"`, `"Comedy"` |
| `status` | String(20) | Watch status | `"Plan to Watch"`, `"Watched"` |
| `review_notes` | Text | Brief personal review | `"Mind-bending visual masterpiece!"` |

### 🛠️ Required Routes & Functionality
- `GET /`: Grid of movies with platform badges (e.g., red badge for Netflix, blue for Prime).
- `POST /add`: Form to add a new movie with title, platform, and genre.
- `GET /toggle-status/<id>`: Mark as "Watched" vs "Plan to Watch".
- `POST /edit/<id>`: Add personal review notes and rating after watching.
- `POST /delete/<id>`: Remove movie from watchlist.

### 🌟 Bonus Challenge (MSc IT Distinction)
Allow filtering by platform (e.g., show only `"Netflix"` titles).

---

## 📌 Project 6: Daily Habit & Streak Tracker

### 🎯 Problem Context
Developing productive habits (like coding 1 hour daily, reading research papers, drinking 2L of water, or exercising) requires consistency. Build a daily habit streak tracker.

### 🗂️ Data Schema / Model
| Field | Type | Description | Example |
|---|---|---|---|
| `id` | Integer | Primary key | `1` |
| `habit_name` | String(100) | Habit description | `"Solve 1 LeetCode Problem"` |
| `target_days` | Integer | Target goal (days) | `30` |
| `current_streak`| Integer | Consecutive days completed | `7` |
| `completed_today`| Boolean | Done today checkmark | `True` / `False` |

### 🛠️ Required Routes & Functionality
- `GET /`: Daily checklist showing each habit, current streak badge (🔥 `7 Days`), and checkmark.
- `POST /add`: Create a new habit with name and target days.
- `GET /check-in/<id>`: Click button to mark "Completed Today" ➔ increments `current_streak += 1`.
- `GET /reset/<id>`: Reset streak to 0 if a day was missed.
- `POST /delete/<id>`: Delete habit.

### 🌟 Bonus Challenge (MSc IT Distinction)
Include a congratulatory banner when a student reaches their target streak!

---

## 📊 Student Grading Rubric (Total: 50 Marks)

| Criteria | Description | Marks |
|---|---|:---:|
| **1. Routing & Architecture** | Clean URL design (`@app.route`), correct HTTP methods (`GET`/`POST`), and proper redirects (`url_for`). | 10 |
| **2. CRUD Implementation** | All four operations (Create, Read, Update, Delete) are fully functional without crashes. | 15 |
| **3. Templates & Jinja2** | Template inheritance (`base.html`), loops (`{% for %}`), conditionals (`{% if %}`), and form bindings. | 10 |
| **4. UI/UX & Feedback** | Clean styling, intuitive buttons, and user feedback messages (alerts / flash). | 5 |
| **5. Data Integrity & Validation** | Prevents empty inputs, validates data formats (numbers, emails), and handles errors gracefully. | 10 |
| **Total** | | **50** |

---

## 💡 Quick Starter Template (`app.py` skeleton)

Students can use this starting scaffold for any of the above projects:

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Define Your Model Here ---
# class Item(db.Model):
#     ...

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # READ
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_item():
    # CREATE
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle_item(id):
    # UPDATE
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_item(id):
    # DELETE
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```
