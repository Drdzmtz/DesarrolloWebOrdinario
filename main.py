from flask import Flask

def main():

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