from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signin")
def signIn():
    return render_template("login.html")

@app.route("/signup")
def signUp():
    return render_template("signUp.html")
