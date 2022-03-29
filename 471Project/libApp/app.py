from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def loginPage():
    return render_template("login.html")

@app.route("/emp_login")
def loginPage():
    return render_template("emplogin.html")

@app.route("/about")
def loginPage():
    return render_template("about.html")

@app.route("/contact")
def loginPage():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()