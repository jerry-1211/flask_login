from flask import Flask,redirect,render_template,url_for
from flask import request,flash,session
from DB_handler import DBModule

app = Flask(__name__)
app.secret_key = "xcvbsdf@sdfvxcv"  # 아무렇게나 생성
DB = DBModule()

@app.route("/")
def index():
    if "uid" in session :
        user = session["uid"]
    else :
        user = "Login"
    return render_template("index.html",user=user)


@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signin_done",methods=["GET"])
def signin_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")
    if DB.signin(_id_=uid,pwd=pwd,name=name):
        return redirect(url_for("index"))
    else :
        flash("이미 존재하는 아이디입니다.")
        return redirect(url_for("signin"))
    

@app.route("/login")
def login():
    if "uid" in session : 
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/login_done",methods=["GET"])
def login_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    if DB.login(uid,pwd) :
        session["uid"] = uid 
        return redirect(url_for("index"))
    else : 
        flash("아이디가 없거나 비밀번호가 틀립니다.")
        return redirect(url_for("login"))
        
@app.route("/logout")
def logout():
   if "uid" in session :
        session.pop("uid")
        return redirect(url_for("index"))
   else :
       return redirect(url_for("login"))
    
@app.route("/write")
def write():
    if "uid" in session :
        return render_template("write_post.html")
    else :
        return redirect(url_for("login"))
    

@app.route("/write_done",methods=["GET"])
def write_done():
    title = request.args.get("title")
    content = request.args.get("content")
    uid = session.get("uid")
    DB.write_post(uid=uid,content=content,title=title)
    return redirect(url_for("index"))

@app.route("/list")
def post_list():
    post_list = DB.post_list()
    if post_list is None:
        length = 0
    else : 
        length = len(post_list)
    return render_template("post_list.html",post_list=post_list.items(),length=length)


@app.route("/post/<string:pid>")
def post(pid) : 
    post = DB.post_detail(pid=pid)
    return render_template("post_detail.html",post=post)


@app.route("/user/<string:uid>")
def user_post(uid) : 
    u_post = DB.get_user(uid)
    if u_post is None : 
        length = 0
    else : 
        length = len(u_post)
    return render_template("user_detail.html",post_list=u_post,length=length,uid=uid)


if __name__ == "__main__":
    app.run(port=5500,host="0.0.0.0",debug=True)