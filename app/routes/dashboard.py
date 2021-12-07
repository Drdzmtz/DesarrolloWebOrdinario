from flask import Blueprint, jsonify, request, render_template, session, redirect, url_for

from app.controllers import sold_properties, price_bracket

dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/dashboard")
def dashboard():
    
    if not "user" in session:
        return redirect(url_for("index"))

    res = sold_properties.sold_properties()

    labels = []
    data = []
    if "data" in res:
        labels  = res["labels"]
        data    = res["data"]


    res = price_bracket.price_bracket()
    
    price_data = []
    if "data" in res:
        price_data = res["data"]

    return render_template('dashboard.html', labels= labels, data= data, **price_data)
