from src.controllers.order_register import OrderRegister
from src.models.repositories.orders_repository import OrdersRepository
from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from src.views.order_register_view import OrderRegisterView


def order_register_composer():
    conn = db_connection_handler.get_connection()
    order_model = OrdersRepository(conn)
    user_model = UserRepository(conn)
    controller = OrderRegister(order_model, user_model)
    view = OrderRegisterView(controller)

    return view