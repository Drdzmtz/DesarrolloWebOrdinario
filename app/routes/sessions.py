from flask import Blueprint, request, render_template, session, redirect
from flask.helpers import url_for

from app.controllers import authentification

session_routes = Blueprint("session_routes", __name__)


@session_routes.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        session.pop('user', None)

        res = authentification.auth(request.form)

        if "username" in res:
            session["user"] = res["username"]
            
            return redirect(url_for("index"))

        return render_template("login.html", error= res["Error"])

    if "user" in session:
        return redirect(url_for("index"))


    return render_template("login.html")



@session_routes.route("/logout", methods=["POST"])
def logout():
    session.pop('user', None)
    
    return render_template("login.html")
