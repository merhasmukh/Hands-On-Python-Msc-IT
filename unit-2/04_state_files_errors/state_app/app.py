from flask import Flask, render_template, request, session, redirect, url_redirect, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
# Secret key is REQUIRED for sessions and flashing messages
app.secret_key = 'super_secret_key_msc_it'

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Check if user is logged in
    if 'username' in session:
        return f"Logged in as {session['username']}. <br><a href='/upload'>Go to Upload</a> | <a href='/logout'>Logout</a>"
    return "You are not logged in. <br><a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        # Always secure the filename before saving!
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f"File {filename} uploaded successfully! <br><a href='/'>Go Home</a>"
    
    return render_template('upload.html')

# Custom Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1><p>Oops! The page you are looking for does not exist.</p>", 404

if __name__ == '__main__':
    app.run(debug=True, port=5002)
