from flask import Blueprint
from src.routes.verification import verification

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(verification.verification_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    return "Homepage route setup!"