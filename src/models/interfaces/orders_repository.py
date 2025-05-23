from abc import ABC, abstractmethod


class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def registry_order(self, user_id: int, date_order: str, description: str) -> None:
        pass

    @abstractmethod
    def get_orders_by_user(self, user_id: int) -> list[tuple[int, str, str, str]]:
        pass
