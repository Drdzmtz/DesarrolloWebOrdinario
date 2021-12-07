from flask import Blueprint, render_template

content_routes = Blueprint("content_routes", __name__)

@content_routes.route("/requisitos")
def requirements():
    return render_template('requirements.html')

@content_routes.route("/servicios")
def services():
    return render_template('services.html')

@content_routes.route("/nosotros")
def company():
    return render_template('company.html')

@content_routes.route("/mudanzas")
def moving():
    return render_template('moving.html')

@content_routes.route("/seguros")
def insurances():
    return render_template('insurances.html')