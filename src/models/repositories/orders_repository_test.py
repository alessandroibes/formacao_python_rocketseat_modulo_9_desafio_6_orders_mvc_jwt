from unittest.mock import Mock

from src.models.repositories.orders_repository import OrdesRepository


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection():
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())


def test_get_order_by_user():
    user_id = 1

    mock_connection = MockConnection()
    repo = OrdesRepository(mock_connection)

    repo.get_order_by_user(user_id)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, user_id, date_order, description" in cursor.execute.call_args[0][0]
    assert "FROM orders" in cursor.execute.call_args[0][0]
    assert "WHERE user_id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id,)

    cursor.fetchone.assert_called_once()
