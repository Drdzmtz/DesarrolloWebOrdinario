from flask import Flask, render_template

from app.config import SECRET_KEY
from app.routes import properties, contact, content, news, pdf, sessions


def main():

    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(properties.properties_routes, url_prefix="/casas")
    app.register_blueprint(contact.contact_routes, url_prefix="/contacto")
    app.register_blueprint(content.content_routes)
    app.register_blueprint(news.news_routes, url_prefix="/news")
    app.register_blueprint(pdf.pdf_routes, url_prefix="/pdf")
    app.register_blueprint(sessions.session_routes)

    @app.route("/", methods=["GET", "POST"])
    def index():
        return render_template('index.html')

if __name__ == "__main__":
    app = Flask(__name__, template_folder="./app/views", static_folder="./app/static")
    main()
    
    app.run(
        port=5000, 
        debug=True
    )