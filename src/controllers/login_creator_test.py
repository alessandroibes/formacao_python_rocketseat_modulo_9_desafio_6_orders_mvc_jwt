from .login_creator import LoginCreator


class MockUserRepository:
    def get_user_by_username(self, username: str) -> tuple[int, int, str]:
        return (1, username, b"$2b$12$0iAKprs.kCuRQ/ldb4S2bOIh3aEhjYIbxwkO5TN2SmFLjoRDsDEZu")


def test_create():
    repository = MockUserRepository()
    controller = LoginCreator(repository)

    username = "teste"
    password = "tesTando"

    response = controller.create(username, password)

    assert response["access"] is True
    assert response["username"] == username
    assert response["token"] is not None
