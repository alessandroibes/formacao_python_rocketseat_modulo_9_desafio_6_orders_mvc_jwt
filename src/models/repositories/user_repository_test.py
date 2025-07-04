from unittest.mock import Mock

from src.models.repositories.user_repository import UserRepository


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection():
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_registry_user():
    username = "teste"
    password = "Test123"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password)

    mock_connection.commit.assert_called_once()


def test_get_user():
    user_id = 1

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user(user_id)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id,)

    cursor.fetchone.assert_called_once()


def test_get_user_by_username():
    username = "teste"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username(username)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)

    cursor.fetchone.assert_called_once()
