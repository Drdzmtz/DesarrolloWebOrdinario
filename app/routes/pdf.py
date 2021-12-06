from flask import Blueprint, make_response

from app.controllers import generate_pdf

pdf_routes = Blueprint("pdf_routes", __name__)

@pdf_routes.route("/")
def index():
    return "PDFs"

@pdf_routes.route("/<id>", methods=["GET"])
def get_pdf(id:int):

    res = generate_pdf.generate_pdf(id)
    
    if "pdf" in res:
        response = make_response(res["pdf"].encode('latin-1'))
        response.headers.set('Content-Type', 'application/pdf')
    
        return response
        
    return res