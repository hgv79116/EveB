from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.before_request
def load_user(): 
    if request.endpoint != "login": 
        return redirect(url_for("login"))

@app.route("/")
def index(): 
    return "goodmorning"

@app.route("/extension/index/")
def extension_index(): 
    return render_template("extension/index.html")

@app.route("/login")
def login(): 
    return render_template("auth/login.html")