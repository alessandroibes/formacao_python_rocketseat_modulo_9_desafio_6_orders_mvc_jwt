from datetime import datetime
from unittest.mock import Mock

from src.models.repositories.orders_repository import OrdesRepository


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection():
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_registry_order():
    user_id = 1
    date_order = datetime.now().isoformat()
    description = "Pizza 4 Queijos"

    mock_connection = MockConnection()
    repo = OrdesRepository(mock_connection)

    repo.registry_order(user_id, date_order, description)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO orders" in cursor.execute.call_args[0][0]
    assert "(user_id, date_order, description)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id, date_order, description)

    mock_connection.commit.assert_called_once()


def test_get_orders_by_user():
    user_id = 1

    mock_connection = MockConnection()
    repo = OrdesRepository(mock_connection)

    repo.get_orders_by_user(user_id)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, user_id, date_order, description" in cursor.execute.call_args[0][0]
    assert "FROM orders" in cursor.execute.call_args[0][0]
    assert "WHERE user_id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id,)

    cursor.fetchone.assert_called_once()
