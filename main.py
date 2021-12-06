from flask import Flask, render_template
from app.routes import properties, contact, content, news, pdf

def main():

    app.register_blueprint(properties.properties_routes, url_prefix="/casas")
    app.register_blueprint(contact.contact_routes)
    app.register_blueprint(content.content_routes)
    app.register_blueprint(news.news_routes, url_prefix="/news")
    app.register_blueprint(pdf.pdf_routes, url_prefix="/pdf")

    @app.route("/")
    def index():
        return render_template('index.html')


if __name__ == "__main__":
    app = Flask(__name__, template_folder="./app/views", static_folder="./app/static")
    main()

    app.run(
        port=5000, 
        debug=True
    )