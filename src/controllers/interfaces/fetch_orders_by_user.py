from abc import ABC, abstractmethod


class FetchOrdersByUserInterface(ABC):

    @abstractmethod
    def get_orders_by_user(self, user_id: int) -> list[dict]:
        pass
