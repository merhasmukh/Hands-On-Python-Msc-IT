"""
02_exercises.py — Flask Framework
==================================
MSc (IT) — Unit 2: Web Application Development with Flask and Databases

Instructions:
- These exercises require you to write a mini Flask app.
- Write your code below and run this file (`python 02_exercises.py`).
- Then open your browser at http://127.0.0.1:5000/
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

# ===========================================================================
# Exercise 1: Basic Route
# ===========================================================================
"""
Create a route for '/about' that returns an HTML string:
"<h1>About Us</h1><p>We are learning Flask!</p>"
"""
# Write your code here:


# ===========================================================================
# Exercise 2: Dynamic Route
# ===========================================================================
"""
Create a route for '/square/<int:number>' that calculates the square of 
the number and returns a string like: "The square of 5 is 25."
"""
# Write your code here:


# ===========================================================================
# Exercise 3: Simple Form (GET and POST)
# ===========================================================================
"""
Create a route for '/contact' that accepts both GET and POST methods.
- If GET: Return an HTML form with a 'message' input field and a submit button.
- If POST: Get the 'message' from the form and return:
  "Thank you! We received your message: [MESSAGE]"

Hint: You can use render_template_string() to render raw HTML strings if you don't 
want to create separate .html files for this exercise.
"""
# Write your code here:


if __name__ == "__main__":
    print("=" * 60)
    print("  Starting Flask Server for Exercises...")
    print("  Check http://127.0.0.1:5000/ in your browser.")
    print("=" * 60)
    app.run(debug=True)
