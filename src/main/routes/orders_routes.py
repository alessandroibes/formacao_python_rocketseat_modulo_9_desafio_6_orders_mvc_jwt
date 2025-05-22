from flask import Blueprint, jsonify, request

from src.errors.error_handler import handler_error
from src.main.composer.order_register_composer import order_register_composer
from src.main.middlewares.auth_jwt import auth_jwt_verify
from src.views.http_types.http_request import HttpRequest


orders_routes_bp = Blueprint("orders_routes", __name__)


@orders_routes_bp.route("/orders/registry", methods=["POST"])
def registry_order():
    try:
        token_infos = auth_jwt_verify()

        http_request = HttpRequest(
            body=request.json,
            token_infos=token_infos,
            headers=request.headers
        )
        http_response = order_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code
