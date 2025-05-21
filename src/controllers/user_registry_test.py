from .user_registry import UserRegister


class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attribute = {}

    def registry_user(self, username, password) -> None:
        self.registry_user_attribute["username"] = username
        self.registry_user_attribute["password"] = password


def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)

    username = "teste"
    password = "tesTando"

    response = controller.registry(username, password)
    
    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.registry_user_attribute["username"] == username
    assert repository.registry_user_attribute["password"] is not None
    assert repository.registry_user_attribute["password"] != password
