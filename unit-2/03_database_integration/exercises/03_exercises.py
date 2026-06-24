"""
03_exercises.py — Database Integration (SQLAlchemy)
===================================================
MSc (IT) — Unit 2: Web Application Development with Flask and Databases

Instructions:
- Below is a basic setup for Flask-SQLAlchemy.
- Complete the exercises inside the app.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'exercise_books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ===========================================================================
# Exercise 1: Define a Model
# ===========================================================================
"""
Define a `Book` model with the following columns:
- id (Integer, Primary Key)
- title (String(150), Not Null)
- author (String(100), Not Null)
- year (Integer)
"""

# Write your Book class here:
# class Book(db.Model):
#    ...


# Create the tables (do not change this)
with app.app_context():
    # db.create_all() # Uncomment this once your model is defined
    pass

# ===========================================================================
# Exercise 2: Insert Data using ORM
# ===========================================================================
"""
Write a route `/add_book` that inserts a book into the database.
You can hardcode the book details for this exercise, e.g., "The Hobbit" by "J.R.R. Tolkien", year 1937.
"""
@app.route('/add_book')
def add_book():
    # Write your code here:
    
    return "Book added!"

# ===========================================================================
# Exercise 3: Query Data using ORM
# ===========================================================================
"""
Write a route `/books` that queries all books from the database and returns 
them as a formatted string.
"""
@app.route('/books')
def list_books():
    # Write your code here:
    
    return "List of books will appear here."

if __name__ == "__main__":
    print("=" * 60)
    print("  Starting Flask Server for Exercises...")
    print("  Check http://127.0.0.1:5000/add_book and /books")
    print("=" * 60)
    app.run(debug=True)
