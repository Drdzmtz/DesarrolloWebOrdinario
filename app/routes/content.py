from flask import Blueprint

content_routes = Blueprint("content_routes", __name__)

@content_routes.route("/requisitos")
def requirements():
    return "REQUESITOS"