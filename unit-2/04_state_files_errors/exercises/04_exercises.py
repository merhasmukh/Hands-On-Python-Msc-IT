"""
04_exercises.py — State, Files, and Errors
==========================================
MSc (IT) — Unit 2: Web Application Development with Flask and Databases

Instructions:
- Below is a basic setup for a Flask app testing sessions and file uploads.
- Complete the exercises inside the app.
"""

from flask import Flask, session, request, redirect

app = Flask(__name__)
# Exercise 1 part A: Set the secret key here!
app.secret_key = "REPLACE_ME_WITH_A_SECRET_KEY"

# ===========================================================================
# Exercise 1: Session Variables
# ===========================================================================
"""
Write a route `/set_theme` that accepts a query parameter `?color=...`
Store this color in the session under the key 'theme'.
Then redirect to the root route `/`.
"""
@app.route('/set_theme')
def set_theme():
    # Write your code here:
    pass


@app.route('/')
def home():
    # Exercise 1 part B: Read the 'theme' from the session. 
    # If not set, default to 'white'.
    theme_color = "white" # Update this line!
    
    return f"""
    <body style='background-color: {theme_color};'>
        <h1>Welcome!</h1>
        <p>Current theme: {theme_color}</p>
        <a href='/set_theme?color=lightblue'>Set Light Blue Theme</a> | 
        <a href='/set_theme?color=lightgreen'>Set Light Green Theme</a>
    </body>
    """

# ===========================================================================
# Exercise 2: File Upload Route Setup
# ===========================================================================
"""
Write a route `/profile_pic` that accepts GET and POST.
- GET: Return a simple HTML form with a file input (name="profile_pic"). 
  Remember the enctype!
- POST: Receive the file, print its filename to the console, and return "Success".
"""
@app.route('/profile_pic', methods=['GET', 'POST'])
def profile_pic():
    # Write your code here:
    return "Not implemented yet."

if __name__ == "__main__":
    print("=" * 60)
    print("  Starting Flask Server for Exercises...")
    print("  Check http://127.0.0.1:5000/")
    print("=" * 60)
    app.run(debug=True)
