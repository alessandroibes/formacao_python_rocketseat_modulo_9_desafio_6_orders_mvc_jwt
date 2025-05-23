from src.models.repositories.orders_repository import OrdersRepositoryInterface
from .interfaces.fetch_orders_by_user import FetchOrdersByUserInterface


class FetchOrdersByUser(FetchOrdersByUserInterface):
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def get_orders_by_user(self, user_id: int) -> list[dict]:
        orders = self.__orders_repository.get_orders_by_user(user_id)
        print(orders)
        formated_response = self.__format_response(orders)
        return formated_response

    def __format_response(self, orders: list[tuple[int, str, str, str]]) -> list[dict]:
        return [{
            "id": order[0],
            "user_id": order[1],
            "date_order": order[2],
            "description": order[3]
        } for order in orders]
