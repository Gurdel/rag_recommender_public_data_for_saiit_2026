import sqlite3


class UsersRepository:

    def __init__(
        self,
        db_path: str
    ):

        self.db_path = db_path

    def get_user_ratings(
        self,
        user_id: int
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        rows = conn.execute(
            """
            SELECT
                book_id,
                rating
            FROM user_ratings
            WHERE user_id = ?
            """,
            (user_id,)
        ).fetchall()

        conn.close()

        return [
            {
                "book_id": row[0],
                "rating": row[1]
            }
            for row in rows
        ]

    def save_rating(
        self,
        user_id: int,
        book_id: str,
        rating: int
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        conn.execute(
            """
            INSERT INTO user_ratings
            (
                user_id,
                book_id,
                rating
            )
            VALUES (?, ?, ?)

            ON CONFLICT(
                user_id,
                book_id
            )
            DO UPDATE SET

            rating=excluded.rating
            """,
            (
                user_id,
                book_id,
                rating
            )
        )

        conn.commit()

        conn.close()

    def add_interaction(
        self,
        user_id: int,
        book_id: str,
        interaction_type: str
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        conn.execute(
            """
            INSERT INTO user_interactions
            (
                user_id,
                book_id,
                interaction_type
            )
            VALUES (?, ?, ?)
            """,
            (
                user_id,
                book_id,
                interaction_type
            )
        )

        conn.commit()

        conn.close()
