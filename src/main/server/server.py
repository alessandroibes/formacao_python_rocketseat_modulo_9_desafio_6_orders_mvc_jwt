from flask import Flask

from src.models.settings.db_connection_handler import db_connection_handler

# Blueprints
from src.main.routes.order_routes import order_routes_bp


db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(order_routes_bp)
