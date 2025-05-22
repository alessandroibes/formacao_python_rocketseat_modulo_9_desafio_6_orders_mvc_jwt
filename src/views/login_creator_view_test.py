import pytest

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .login_creator_view import LoginCreatorView


class MockController:
    def create(self, username, password):
        return {
            "access": True,
            "username": username,
            "token": "0123456789"
        }


def test_handler_login_creator():
    body = {
        "username": "teste",
        "password": "tesTando"
    }
    request = HttpRequest(body=body)
    
    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)
    response = login_creator_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {
        "data": {
            "access": True,
            "username": "teste",
            "token": "0123456789"
        }
    }
    assert response.status_code == 200


def test_handler_login_creator_with_validation_error():
    body = {
        "password": "tesTando"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        login_creator_view.handle(request)
