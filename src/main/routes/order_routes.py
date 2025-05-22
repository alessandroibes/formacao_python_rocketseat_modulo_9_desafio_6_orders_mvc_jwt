from flask import Blueprint, jsonify


order_routes_bp = Blueprint("order_routes", __name__)


@order_routes_bp.route("/", methods=["GET"])
def health_check():
    return jsonify({ "health": "Check OK" }), 200
