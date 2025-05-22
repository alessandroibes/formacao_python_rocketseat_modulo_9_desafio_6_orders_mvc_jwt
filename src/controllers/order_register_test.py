from datetime import datetime

from .order_register import OrderRegister


class MockOrdersRepository:
    def registry_order(self, user_id: int, date_order: str, description: str):
        pass


class MockUserRepository:
    def get_user(self, user_id):
        return (12, "teste", "0123456789")


def test_order_registry():
    orders_repository = MockOrdersRepository()
    user_repository = MockUserRepository()
    controller = OrderRegister(orders_repository, user_repository)

    user_id = 12
    description = "Pizza 4 Queijos"

    response = controller.registry(user_id, description)

    assert response["data"]["type"] == "Order"
    assert response["data"]["count"] == 1
    assert isinstance(datetime.fromisoformat(response["data"]["inserted_date"]), datetime)
