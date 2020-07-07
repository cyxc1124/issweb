from flask import Blueprint, render_template, redirect

login = Blueprint('login', __name__, url_prefix='/')

@login.route("/login")
def login():
    return render_template("login.html")