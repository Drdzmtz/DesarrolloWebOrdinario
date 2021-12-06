from flask import Blueprint, jsonify, request

from app.controllers import send_mail

contact_routes = Blueprint("contact_routes", __name__)

@contact_routes.route("/")
def contact():
    return "CONTACTANOS"

@contact_routes.route("/send-mail", methods=["POST"])
def contact_mail():
    return send_mail.send_mail(request.form)
