from abc import ABC, abstractmethod


class OrderRegisterInterface(ABC):
    
    @abstractmethod
    def registry(self, user_id: int, description: str) -> None:
        pass