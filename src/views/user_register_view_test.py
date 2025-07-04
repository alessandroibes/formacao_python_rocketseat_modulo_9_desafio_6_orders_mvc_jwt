import pytest

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView


class MockController:
    def registry(self, username, password):
        return { "teste": "outro teste" }


def test_handler_user_register():
    body = {
        "username": "teste",
        "password": "tesTando"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == { 'data': { 'teste': 'outro teste'} }
    assert response.status_code == 201


def test_handler_user_register_with_validation_error():
    body = {
        "password": "tesTando"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)
