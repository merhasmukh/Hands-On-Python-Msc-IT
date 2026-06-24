from flask import Flask, render_template, request

app = Flask(__name__)

# Basic Route
@app.route("/")
def home():
    return render_template("index.html")

# Dynamic Route
@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", person_name=name)

# Handling Forms
@app.route("/search", methods=["GET", "POST"])
def search():
    query = None
    if request.method == "POST":
        # Get data from the form
        query = request.form.get("search_query")
    return render_template("search.html", query=query)

if __name__ == "__main__":
    app.run(debug=True)
