from flask import Blueprint

from app.controllers import get_properties

properties_routes = Blueprint("properties_routes", __name__)

@properties_routes.route("/casas")
def houses():
    return get_properties.get_properties()

@properties_routes.route("/casas/<id>")
def house_by_id(id:int):
    return get_properties.get_properties(id)