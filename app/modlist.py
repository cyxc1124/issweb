from flask import Blueprint, render_template

modlist = Blueprint('modlist', __name__, url_prefix='/modlist')


@modlist.route("/")
def mod():
    return render_template("modlist.html")