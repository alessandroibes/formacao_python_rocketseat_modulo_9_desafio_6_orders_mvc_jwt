import pytest

from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator


username = "teste"
password = "tesTando"
hashed_password = PasswordHandler().encrypt_password(password)


class MockUserRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)


def test_create():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username, password)

    assert response["access"] is True
    assert response["username"] == username
    assert response["token"] is not None


def test_create_with_wrong_password():
    login_creator = LoginCreator(MockUserRepository())

    with pytest.raises(Exception):
        login_creator.create(username, "senhaErrada")
