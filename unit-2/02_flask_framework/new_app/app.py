from flask import Flask,render_template,request, Blueprint,jsonify
from api_routes import api_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(api_bp,url_prefix="/api")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Step 2: Define the Student Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)       # Unique ID
    name = db.Column(db.String(100), nullable=False)   # Name cannot be blank
    status = db.Column(db.String(100), nullable=False) # Course name
    due_date = db.Column(db.DateTime(),nullable=False)                    # Grade (e.g. 'A+', 'B')

    def __repr__(self):
        return f"<Student #{self.id}: {self.name} ({self.course}) - Grade: {self.grade}>"

def get_db():    
    with app.app_context():
        db.create_all()

@app.route("/db_create")
def db_create():
    get_db()
    return "db created"

@app.route("/",methods=['GET','POST'])
def root():
    print(request.method)
    if request.method=='GET':
        return "Hello From Flask"
    else:
        return "Invalid Request"


@app.route("/add",methods=['POST'])
def add_todo():
    todo_name=request.form.get("name")
    with app.app_context():
        # 1. Create a Student object
        t1 = Todo(name=todo_name, status="Python", due_date="A")

        # 2. Stage and save
        db.session.add(t1)
        db.session.commit()

    print(f"✅ Step 4 Complete: Student saved! Auto-assigned ID is: {s1.id}")


@app.route("/get",methods=['GET'])
def get_todo():
    with app.app_context():
        # 1. Create a Student object
        t1 = Todo.query.all()

    print(f"✅ Step 4 Complete: Student saved! Auto-assigned ID is: {s1.id}")

    

@app.route("/search",methods=['GET','POST'])
def search():
    print(request.method)
    if request.method=='POST':
        data=request.form.get("search_query")
        print(data)
        return jsonify({'data':data})
    else:
        return "Invalid Request"

@app.route("/home")
def home():
    name="Vijay"
    courses=['MCA','BCA','PGDCA','MSc(IT)']
    return render_template("greet.html",name=name,courses=courses)

@app.route("/root/name/<string:user_name>/user_id/<int:user_id>")
def hasmukh(user_name):
    courses=['MCA','BCA','PGDCA','MSc(IT)']
    return render_template("greet.html",name=user_name,courses=courses)


if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001,debug=True)
