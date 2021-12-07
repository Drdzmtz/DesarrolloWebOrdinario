from flask import Blueprint, jsonify, request, session

from app.controllers import get_news, add_news

news_routes = Blueprint("news_routes", __name__)

@news_routes.route("/", methods=["GET"])
def news():
    news = get_news.get_news()

    return jsonify(**news)

@news_routes.route("/", methods=["POST"])
def post_news():

    news = {"Error": "Usuario no autorizado"}

    if  "user" in session:
        news = add_news.add_news(request.form)

    return jsonify(**news)