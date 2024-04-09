from flask import Flask,redirect,render_template,url_for
from flask import request,flash,session
from DB_handler import DBModule

app = Flask(__name__)
app.secret_key = "xcvbsdf@sdfvxcv"  # 아무렇게나 생성
DB = DBModule()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signin_done",methods=["GET"])
def signin_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")
    if DB.singin(_id_=uid,pwd=pwd,name=name):
        return redirect(url_for("index"))
    else :
        flash("이미 존재하는 아이디입니다.")
        return redirect(url_for("signin"))
    

@app.route("/login")
def login():
    pass

@app.route("/login_done",methods=["GET"])
def login_done():
    pass

@app.route("/logout")
def logout():
    pass

if __name__ == "__main__":
    app.run(port=5500,host="0.0.0.0",debug=True)