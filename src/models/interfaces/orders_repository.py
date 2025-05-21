from abc import ABC, abstractmethod


class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def get_order_by_user(self, user_id: int) -> tuple[int, str, str, str]:
        pass
