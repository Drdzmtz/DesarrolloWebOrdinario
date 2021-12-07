from flask import Flask, render_template, session, redirect, url_for

from app.config import SECRET_KEY
from app.routes import properties, contact, content, news, pdf, sessions, dashboard


def main():

    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(properties.properties_routes, url_prefix="/casas")
    app.register_blueprint(contact.contact_routes, url_prefix="/contacto")
    app.register_blueprint(content.content_routes)
    app.register_blueprint(news.news_routes, url_prefix="/news")
    app.register_blueprint(pdf.pdf_routes, url_prefix="/pdf")
    app.register_blueprint(dashboard.dashboard_routes)
    app.register_blueprint(sessions.session_routes)

    @app.route("/", methods=["GET", "POST"])
    def index():

        if "user" in session:
            return redirect(url_for("dashboard_routes.dashboard"))

        return render_template('index.html')

if __name__ == "__main__":
    app = Flask(__name__, template_folder="./app/views", static_folder="./app/static")
    main()
    
    app.run(
        port=5000, 
        debug=True
    )