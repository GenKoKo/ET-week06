from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'root'
app.config["MYSQL_DB"] = 'wk6'

mysql = MySQL(app)

@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        name = request.form["name"]
        account = request.form["account"]
        password = request.form["password"]
        my_cursor = mysql.connection.cursor()
        my_cursor.execute("INSERT INTO user(name, account, password) VALUES(%s, %s, %s)",(name,account,password))
        mysql.connection.commit()
        my_cursor.close()

    return 'success'

    return render_template('test2.html')

if __name__ == "__main__":
    app.run(debug=True)