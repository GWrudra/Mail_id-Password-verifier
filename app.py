from flask import Flask, render_template, request, redirect, session
import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    return redirect("/login")

#Database creation
def init_db():
    conn= sqlite3.connect('users.db')
    c=conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

#Validation
def valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

def valid_password(pw):
    if len(pw) < 8:
        return False
    if not any(c.isdigit() for c in pw):
        return False
    if not any(c.islower() for c in pw):
        return False
    if not any(c.isupper() for c in pw):
        return False
    if not any(c in "!@#$%^&*_-+?." for c in pw):
        return False
    return True

#Create Account Page
@app.route("/create", methods=["GET", "POST"])
def create_account():
    message = ""

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if not valid_email(email):
            message = "Invalid Email ❌"
        elif not valid_password(password):
            message = "Weak Password ❌"
        else:
            hashed_pw = generate_password_hash(password)
            try:
                conn = sqlite3.connect("users.db")
                c = conn.cursor()
                c.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                          (email, hashed_pw))
                conn.commit()
                conn.close()
                return redirect("/login")
            except:
                message = "User already exists ❌"

    return render_template("create.html", message=message)

#Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE email=?", (email,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            session["user"] = email
            return redirect("/dashboard")
        else:
            message = "Invalid Credentials ❌"

    return render_template("login.html", message=message)

#Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", email=session["user"])
    return redirect("/login")

#Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)