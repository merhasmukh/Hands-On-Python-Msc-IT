"""
03_exercises.py — Database Integration with Flask-SQLAlchemy
============================================================
Unit 2: Web Application Development with Flask and Databases
Course: MSc (IT) — Hands-On Python

Learning Outcomes:
------------------
1. Define declarative models with appropriate data types and constraints.
2. Implement robust CRUD functions using the SQLAlchemy session.
3. Wire ORM database operations into Flask routes.
4. Establish One-to-Many relational foreign keys.

How to Run:
-----------
- Run the interactive Flask server:
    python 03_exercises.py

- Run the automated self-grading test runner:
    python 03_exercises.py --test
"""

import sys
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database path
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ===========================================================================
# 📝 EXERCISE 1: Define the Book Model
# ===========================================================================
# Define a model named `Book` representing the `books` table with columns:
# - id: Integer, Primary Key
# - title: String(150), nullable=False
# - author: String(100), nullable=False
# - price: Float, nullable=False
# - published_year: Integer, nullable=True
# - in_stock: Boolean, default=True, nullable=False
#
# Hint:
# class Book(db.Model):
#     __tablename__ = 'books'
#     id = db.Column(db.Integer, primary_key=True)
#     ...
# ===========================================================================

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    published_year = db.Column(db.Integer, nullable=True)
    in_stock = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        """Helper to convert ORM model instance into JSON-serializable dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "published_year": self.published_year,
            "in_stock": self.in_stock
        }

    def __repr__(self):
        return f"<Book #{self.id} '{self.title}' by {self.author}>"


# Create tables inside application context
with app.app_context():
    db.create_all()


# ===========================================================================
# 📝 EXERCISE 2: Implement ORM Helper Functions (CRUD)
# ===========================================================================

def add_book(title, author, price, published_year=None, in_stock=True):
    """
    Creates a new Book record, adds it to the session, commits, and returns it.
    """
    # TODO: Complete this function
    new_book = Book(
        title=title,
        author=author,
        price=price,
        published_year=published_year,
        in_stock=in_stock
    )
    db.session.add(new_book)
    db.session.commit()
    return new_book


def get_all_books():
    """
    Queries and returns all books ordered by title ascending.
    """
    # TODO: Complete this function using Book.query
    return Book.query.order_by(Book.title.asc()).all()


def find_books_by_author(author_name):
    """
    Returns a list of all books matching the specified author (case-insensitive search).
    """
    # TODO: Complete this function using filter() with ilike or filter_by()
    pattern = f"%{author_name}%"
    return Book.query.filter(Book.author.ilike(pattern)).all()


def update_book_price(book_id, new_price):
    """
    Retrieves the book with the given ID, updates its price, commits, and returns the book.
    Returns None if book_id does not exist.
    """
    # TODO: Complete this function using db.session.get(Book, book_id)
    book = db.session.get(Book, book_id)
    if book:
        book.price = float(new_price)
        db.session.commit()
    return book


def delete_book(book_id):
    """
    Deletes the book with the given ID from the database.
    Returns True if deleted, False if not found.
    """
    # TODO: Complete this function using db.session.delete()
    book = db.session.get(Book, book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    return False


# ===========================================================================
# 📝 EXERCISE 3: Flask Web Routes Connecting to Database
# ===========================================================================

@app.route('/books', methods=['GET'])
def list_books_route():
    """
    GET /books:
    Queries all books from the database and returns a JSON list of dictionaries.
    Status code: 200 OK
    """
    books = get_all_books()
    return jsonify([b.to_dict() for b in books]), 200


@app.route('/books/add', methods=['POST'])
def add_book_route():
    """
    POST /books/add:
    Extracts 'title', 'author', 'price', and optional 'published_year' from JSON or form.
    Validates required fields; returns 400 if any missing.
    Otherwise creates book, saves to DB, and returns JSON of created book with 201 Created.
    """
    data = request.get_json(silent=True) or request.form

    title = data.get('title')
    author = data.get('author')
    price = data.get('price')
    year = data.get('published_year')

    if not title or not author or price is None:
        return jsonify({"error": "Missing required fields (title, author, price)"}), 400

    try:
        price = float(price)
        year = int(year) if year else None
    except ValueError:
        return jsonify({"error": "Invalid price or published_year format"}), 400

    book = add_book(title, author, price, year)
    return jsonify(book.to_dict()), 201


@app.route('/books/<int:book_id>/discount/<float:percent>', methods=['POST'])
def apply_discount_route(book_id, percent):
    """
    POST /books/<book_id>/discount/<percent>:
    Reduces the book's price by the given percentage (e.g., 20.0 = 20% off).
    Returns 404 if book not found.
    Returns updated book JSON with 200 OK.
    """
    book = db.session.get(Book, book_id)
    if not book:
        return jsonify({"error": f"Book #{book_id} not found"}), 404

    discount_factor = (100.0 - percent) / 100.0
    new_price = round(book.price * discount_factor, 2)
    update_book_price(book_id, new_price)

    return jsonify(book.to_dict()), 200


# ===========================================================================
# 📝 EXERCISE 4 (MSc IT Master Challenge): Relational Extension
# ===========================================================================
# Define a Publisher model and associate each Book with a Publisher (1:N).
# - Publisher model with: id, name (unique), country
# - Link Book to Publisher using ForeignKey and db.relationship
# ===========================================================================

class Publisher(db.Model):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    country = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Publisher {self.name}>"


# ===========================================================================
# 🧪 Automated Self-Grading Verification Test Suite
# ===========================================================================

def run_tests():
    """Runs automated verification tests for student lab submissions."""
    print("\n" + "=" * 65)
    print("  🧪 Running Automated Test Suite for 03_exercises.py...")
    print("=" * 65)

    passed = 0
    total = 5

    with app.app_context():
        # Clear tables for isolated testing
        db.drop_all()
        db.create_all()

        # --- Test 1: Model Creation & add_book() ---
        try:
            b1 = add_book("Clean Code", "Robert C. Martin", 42.50, 2008)
            assert b1.id is not None, "Book ID was not generated"
            assert b1.title == "Clean Code", "Book title mismatch"
            print("✅ Test 1 Passed: Book model instantiation and add_book() function")
            passed += 1
        except Exception as e:
            print(f"❌ Test 1 Failed: {e}")

        # --- Test 2: get_all_books() and find_books_by_author() ---
        try:
            add_book("The Pragmatic Programmer", "Andy Hunt & Dave Thomas", 45.00, 1999)
            add_book("Clean Architecture", "Robert C. Martin", 39.99, 2017)

            all_books = get_all_books()
            assert len(all_books) == 3, f"Expected 3 books, got {len(all_books)}"

            martin_books = find_books_by_author("Martin")
            assert len(martin_books) == 2, f"Expected 2 Martin books, got {len(martin_books)}"
            print("✅ Test 2 Passed: Queries get_all_books() and find_books_by_author()")
            passed += 1
        except Exception as e:
            print(f"❌ Test 2 Failed: {e}")

        # --- Test 3: update_book_price() and delete_book() ---
        try:
            updated = update_book_price(b1.id, 35.00)
            assert updated.price == 35.00, "Price was not updated"

            del_res = delete_book(b1.id)
            assert del_res is True, "delete_book should return True on success"
            assert db.session.get(Book, b1.id) is None, "Book still found after deletion"
            print("✅ Test 3 Passed: update_book_price() and delete_book()")
            passed += 1
        except Exception as e:
            print(f"❌ Test 3 Failed: {e}")

    # --- Test 4 & 5: Flask Web Routes via test_client ---
    with app.test_client() as client:
        try:
            # Test POST /books/add
            res = client.post('/books/add', json={
                "title": "Design Patterns",
                "author": "Erich Gamma et al.",
                "price": 54.95,
                "published_year": 1994
            })
            assert res.status_code == 201, f"Expected 201, got {res.status_code}"
            data = res.get_json()
            new_id = data["id"]
            print("✅ Test 4 Passed: Route POST /books/add validates input and inserts record")
            passed += 1

            # Test POST /books/<id>/discount/<percent>
            disc_res = client.post(f'/books/{new_id}/discount/10.0')
            assert disc_res.status_code == 200, f"Expected 200, got {disc_res.status_code}"
            disc_data = disc_res.get_json()
            assert disc_data["price"] == 49.46, f"Expected 49.46, got {disc_data['price']}"
            print("✅ Test 5 Passed: Route POST /books/<id>/discount/<percent> calculates discount")
            passed += 1
        except Exception as e:
            print(f"❌ Route Tests Failed: {e}")

    print("\n" + "-" * 65)
    print(f"  🏁 Final Result: {passed}/{total} Tests Passed ({int(passed/total*100)}%)")
    print("=" * 65 + "\n")


# ===========================================================================
# 🚀 Server Launcher
# ===========================================================================
if __name__ == '__main__':
    if '--test' in sys.argv:
        run_tests()
    else:
        print("=" * 65)
        print("  📚 MSc IT Library ORM Server Running")
        print("  📍 View Books : http://127.0.0.1:5000/books")
        print("  🧪 Run Tests  : python 03_exercises.py --test")
        print("=" * 65)
        app.run(debug=True, port=5000)
