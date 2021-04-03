from flask import Flask,request,redirect,render_template, session,url_for, flash
import json
from flask_mysqldb import MySQL
# import MySQLdb.cursors



app = Flask(__name__,
            static_folder="static",
            static_url_path="/"
        )
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'root'
app.config["MYSQL_DB"] = 'wk6'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/signup", methods = ['POST'])
def signup():
    
    name = request.form["n"]
    username = request.form["a"]
    password = request.form["p"]
    #不用MySQLdb.cursors.DictCursor也可以運行
    my_cursor = mysql.connection.cursor()

    #不知為何 必預用[]而不用能()
    my_cursor.execute("SELECT * FROM user WHERE username = %s", [username])
    check_username_exist = my_cursor.fetchone()

    if check_username_exist:
        return redirect(url_for("error", message = 'Account Exist! '))

    else:
        my_cursor.execute("INSERT INTO user(name, username, password) VALUES(%s, %s, %s)",(name,username,password))
        mysql.connection.commit()
        my_cursor.close()
        # flash("Register Success")  #flash應該不是跳出式的訊息
        return redirect(url_for("index"))


@app.route("/member", methods = ["GET","POST"])
def member():

    if "ac" in session:
        my_cursor = mysql.connection.cursor()
        my_cursor.execute("SELECT * FROM user WHERE username = %s", [session['ac']])
        account = my_cursor.fetchone()
        print(account)
        return render_template("/member.html",account=account)

    return redirect(url_for("index"))


@app.route("/signin", methods =["POST"])
def signin():

    username = request.form["a"]
    password = request.form["p"]
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT * FROM user WHERE username = %s and password = %s", [username,password])
    check_username_password_match = my_cursor.fetchone()

    if check_username_password_match:
        print(my_cursor)
        session["ac"] = username
        session["pa"] = password
        print("status: log in")
        print(session)
        return redirect(url_for("member"))

 
    else:
        print(session)
        print("status: login fail")
        return redirect(url_for("error", message="Wrong Account or Password! "))


@app.route("/error")
def error():
    info = request.args.get("message")
    return render_template("/error.html",info=info)

@app.route("/signout")
def signout():
    session.pop("ac",None)
    session.pop("pa", None)
    print("status: log out")
    print(session)
    return redirect(url_for("index"))

if __name__ == "__main__":
#debug=True 不用重啟app.py就能看修正結果 
    app.run(port=3000, debug=True)