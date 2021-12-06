from flask import Flask

from app.routes import properties, contact, content, news

def main():

    app.register_blueprint(properties.properties_routes, url_prefix="/casas")
    app.register_blueprint(contact.contact_routes      )
    app.register_blueprint(content.content_routes      )
    app.register_blueprint(news.news_routes, url_prefix="/news"    )

    @app.route("/")
    def index():
        return "Desarrollo Web"


if __name__ == "__main__":
    app = Flask(__name__, template_folder="./app/views")
    main()

    app.run(
        port=5000, 
        debug=True
    )