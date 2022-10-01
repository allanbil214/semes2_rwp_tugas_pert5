from flask import Flask, render_template, request, session
import mysql.connector

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"

db = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "sia_383" 
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "POST"):
        uname = request.form['uname']
        pwd = request.form['pwd']

        cur = db.cursor()
        cur.execute("select * from user_383 where username_383=%s", (uname,))
        user = cur.fetchone()
        cur.close()

        if (len(user) > 0):
            if (pwd == user[3]):
                session["uname"] = user[2]
                session['pwd'] = user[3]
                session['rname'] = user[1]
                return render_template("home.html")
            else:
                return "Username and Password are NOT Match"
        else:
            return "User with that Username are NOT Found"
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)