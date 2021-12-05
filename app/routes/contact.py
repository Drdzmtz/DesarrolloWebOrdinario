from flask import Blueprint

contact_routes = Blueprint("contact_routes", __name__)

@contact_routes.route("/contacto")
def houses():
    return "CONTACTANOS"