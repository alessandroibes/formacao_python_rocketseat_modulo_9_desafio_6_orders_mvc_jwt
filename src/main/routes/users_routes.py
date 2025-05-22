from flask import Blueprint, jsonify, request

from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_register_composer import user_register_composer
from src.views.http_types.http_request import HttpRequest


users_routes_bp = Blueprint("users_routes", __name__)


@users_routes_bp.route("/users/registry", methods=["POST"])
def registry_user():
    http_request = HttpRequest(body=request.json)
    http_response = user_register_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@users_routes_bp.route("/users/login", methods=["POST"])
def create_login():
    http_request = HttpRequest(body=request.json)
    http_response = login_creator_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code
