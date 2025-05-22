from datetime import datetime, timezone

from src.errors.types.http_not_found import HttpNotFoundError
from src.models.repositories.orders_repository import OrdersRepositoryInterface
from src.models.repositories.user_repository import UserRepository
from .interfaces.order_register import OrderRegisterInterface


class OrderRegister(OrderRegisterInterface):
    def __init__(self, order_repository: OrdersRepositoryInterface, user_repository: UserRepository) -> None:
        self.__order_repository = order_repository
        self.__user_repository = user_repository
    
    def registry(self, user_id: int, description: str) -> dict:
        user = self.__get_user(user_id)
        date_order = datetime.now(timezone.utc)
        self.__registry_order_in_db(user[0], date_order, description)
        formated_response = self.__format_response(date_order)
        return formated_response
    
    def __get_user(self, user_id: int) -> tuple[int, str, str]:
        user = self.__user_repository.get_user(user_id)
        
        if not user: raise HttpNotFoundError("User not found")

        return user

    def __registry_order_in_db(self, user_id: int, date_order: datetime, description: str) -> None:
        self.__order_repository.registry_order(user_id, date_order, description)

    def __format_response(self, date_order: datetime) -> dict:
        return {
            "data": {
                "type": "Order",
                "count": 1,
                "inserted_date": date_order.isoformat()
            }
        }
