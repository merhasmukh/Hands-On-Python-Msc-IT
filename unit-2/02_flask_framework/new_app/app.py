from flask import Flask,render_template,request, Blueprint
from api_routes import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp,url_prefix="/api")

@app.route("/",methods=['GET','POST'])
def root():
    print(request.method)
    if request.method=='GET':
        return "Hello From Flask"
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
    app.run(port=5001,debug=True)
