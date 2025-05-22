import pytest

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .order_register_view import OrderRegisterView


class MockController:
    def registry(self, user_id, description):
        return {
            "data": {
                "type": "Order",
                "count": 1,
                "inserted_date": "2025-05-22T18:09:26.632769+00:00"
            }
        }


def test_handler_order_register():
    body = { "description": "Pizza 4 Queijos" }
    params={ "user_id": "1" }
    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()
    order_register_view = OrderRegisterView(mock_controller)

    response = order_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {
        "data": {
            "type": "Order",
            "count": 1,
            "inserted_date": "2025-05-22T18:09:26.632769+00:00"
        }
    }
    assert response.status_code == 201


def test_handler_order_register_without_user_id():
    body = { "description": "Pizza 4 Queijos" }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    order_register_view = OrderRegisterView(mock_controller)

    with pytest.raises(Exception):
        order_register_view.handle(request)


def test_handler_order_register_without_description():
    body = { }
    params={ "user_id": "1" }
    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()
    order_register_view = OrderRegisterView(mock_controller)

    with pytest.raises(Exception):
        order_register_view.handle(request)


def test_handler_order_register_with_invalid_user_id():
    body = { "description": "Pizza 4 Queijos" }
    params={ "user_id": "a" }
    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()
    order_register_view = OrderRegisterView(mock_controller)

    with pytest.raises(Exception):
        order_register_view.handle(request)


def test_handler_order_register_with_invalid_description():
    body = { "description": True }
    params={ "user_id": "1" }
    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()
    order_register_view = OrderRegisterView(mock_controller)

    with pytest.raises(Exception):
        order_register_view.handle(request)
