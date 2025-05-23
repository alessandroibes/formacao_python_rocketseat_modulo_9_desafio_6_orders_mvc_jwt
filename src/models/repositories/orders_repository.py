from sqlite3 import Connection

from src.models.interfaces.orders_repository import OrdersRepositoryInterface


class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_order(self, user_id: int, date_order: str, description: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO orders
                (user_id, date_order, description)
            VALUES
                (?, ?, ?)
            ''', (user_id, date_order, description)
        )
        self.__conn.commit()

    def get_orders_by_user(self, user_id: int) -> list[tuple[int, str, str, str]]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, user_id, date_order, description
            FROM orders
            WHERE user_id = ?;
            """, (user_id,)
        )

        orders = cursor.fetchall()

        return orders
