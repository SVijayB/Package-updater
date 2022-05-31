from flask.templating import render_template
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, send_from_directory
from src.routes import api_blueprint
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    api_cors_config = {
        "origins": [
            "*",
            "http://localhost:3000",
        ]
    }
    CORS(app, resources={"/*": api_cors_config})
    app.secret_key = os.getenv("API_KEY")

    # Initial Render Page.
    @app.route("/", methods=["GET"])
    def index():
        return """<html>
                    <head>
                        <title>Dyte Internship Assignment</title>
                    </head>
                    <body>
                        <h3>API running successfully!<h3>
                    </body>
                </html>"""

    # Adding Dyte logo as a favicon.
    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "../assets"),
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    # Error handling for pages not present.
    @app.errorhandler(404)
    def page_not_found(e):
        return "ERROR 404: CANNOT GET {}".format(request.path)

    # Registering all the blueprints present in the src/routes folder.
    app.register_blueprint(api_blueprint)
    return app
