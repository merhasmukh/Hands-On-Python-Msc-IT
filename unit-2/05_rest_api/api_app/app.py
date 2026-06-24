from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (list of dictionaries)
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Helper function to find a book by ID
def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

# ---------------------------------------------------------
# REST API Endpoints
# ---------------------------------------------------------

# 1. READ ALL (GET)
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({"status": "success", "data": books}), 200

# 2. READ ONE (GET)
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if book:
        return jsonify({"status": "success", "data": book}), 200
    return jsonify({"status": "error", "message": "Book not found"}), 404

# 3. CREATE (POST)
@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json()
    
    # Basic validation
    if not data or not "title" in data or not "author" in data:
        return jsonify({"status": "error", "message": "Missing title or author"}), 400
    
    # Generate new ID
    new_id = max([b["id"] for b in books]) + 1 if books else 1
    new_book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"]
    }
    
    books.append(new_book)
    return jsonify({"status": "success", "data": new_book}), 201

# 4. UPDATE (PUT)
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({"status": "error", "message": "Book not found"}), 404
        
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
        
    # Update fields
    book["title"] = data.get("title", book["title"])
    book["author"] = data.get("author", book["author"])
    
    return jsonify({"status": "success", "data": book}), 200

# 5. DELETE (DELETE)
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({"status": "error", "message": "Book not found"}), 404
        
    books.remove(book)
    return jsonify({"status": "success", "message": "Book deleted"}), 200

if __name__ == '__main__':
    print("=" * 60)
    print("  Starting REST API Server...")
    print("  Test endpoints with Postman at http://127.0.0.1:5003/api/books")
    print("=" * 60)
    app.run(debug=True, port=5003)
