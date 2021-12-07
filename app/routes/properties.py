from flask import Blueprint, jsonify, request, render_template

from app.controllers import get_properties, add_properties, update_properties

properties_routes = Blueprint("properties_routes", __name__)

@properties_routes.route("/buscar", methods=["GET"])
def houses_page():
    return render_template("houses.html", filters=request.args)

@properties_routes.route("/", methods=["GET"])
def houses():
    properties = get_properties.get_properties(args= request.args)

    return jsonify(**properties)

@properties_routes.route("/<id>", methods=["GET"])
def house_by_id(id:int):
    properties = get_properties.get_properties(id= id)

    return jsonify(**properties)

@properties_routes.route("/", methods=["POST"])
def houses_post():    
    res = add_properties.add_properties(request.form)

    return jsonify(**res)


@properties_routes.route("/", methods=["PUT"])
def houses_put():    
    res = update_properties.update_properties(request.form)

    return jsonify(**res)

@properties_routes.route("/", methods=["PATCH"])
def houses_patch():    
    res = update_properties.patch_properties(request.form)

    return jsonify(**res)