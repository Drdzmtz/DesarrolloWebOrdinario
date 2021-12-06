from flask import Blueprint, jsonify, request

from app.controllers import get_news, add_news

news_routes = Blueprint("news_routes", __name__)

@news_routes.route("/", methods=["GET"])
def news():
    properties = get_news.get_news()

    return jsonify(**properties)

@news_routes.route("/", methods=["POST"])
def post_news():
    properties = add_news.add_news(request.form)

    return jsonify(**properties)