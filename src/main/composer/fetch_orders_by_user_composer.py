from src.controllers.fetch_orders_by_user import FetchOrdersByUser
from src.models.repositories.orders_repository import OrdersRepository
from src.models.settings.db_connection_handler import db_connection_handler
from src.views.fetch_orders_by_user_view import FetchOrderByUserView


def fetch_order_by_user_composer():
    conn = db_connection_handler.get_connection()
    model = OrdersRepository(conn)
    controller = FetchOrdersByUser(model)
    view = FetchOrderByUserView(controller)

    return view
