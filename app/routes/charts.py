from flask import Flask
from flask import render_template

from app.models.House_dal import House_dal
 
app = Flask(__name__)
 
@app.route("/chart1")
def chart1():
    title = 'Reporte de venta de casas'
    labels = ["VENDIDO", "EN VENTA"]
    values = House_dal.select_houses_for_status
    return render_template('chart.html', values=values, labels=labels, title=title)

@app.route("/chart2")
def chart1():
    title = 'Reporte de venta de casas por precios'
    labels = ["<= 250000", "> 250000 AND <= 500000", "> 500000 AND <= 750000", "> 750000 AND <= 1000000", "> 1000000 AND <= 1250000", "> 1250000 AND <= 1500000"]
    values = House_dal.select_houses_for_prices
    return render_template('chart2.html', values=values, labels=labels, title=title)