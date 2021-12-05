from types import MethodType
from flask import Blueprint, jsonify

from app.controllers import get_properties

properties_routes = Blueprint("properties_routes", __name__)

@properties_routes.route("/", methods=["GET"])
def houses():
    properties = get_properties.get_properties()

    return jsonify(**properties)

@properties_routes.route("/<id>", methods=["GET"])
def house_by_id(id:int):
    properties = get_properties.get_properties(id)

    return jsonify(**properties)