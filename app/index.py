from flask import Blueprint, render_template, redirect
import time

index = Blueprint('index', __name__, url_prefix='/')


@index.route("/")
def indexpage():
    return render_template("index.html")


@index.route("/joinus")
def joinus():
    return redirect('https://jq.qq.com/?_wv=1027&k=5XnZwfy')


@index.route("/docs/rcon")
def doc_rcon():
    return render_template("rcon.html")


@index.route("/about")
def about():
    return render_template("aboutxiaocao.html")


@index.route("/zabbix")
def zabbix():
    return render_template("zabbix.html", time=time.time())
