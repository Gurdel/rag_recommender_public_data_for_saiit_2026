import sqlite3


class MetadataLoader:

    def __init__(
        self,
        db_path: str
    ):

        self.db_path = db_path

    def _fetch_list(
        self,
        query: str
    ):

        conn = sqlite3.connect(self.db_path)

        rows = conn.execute(query).fetchall()

        conn.close()

        return sorted([
            r[0]
            for r in rows
            if r[0]
        ])

    def load_authors(self):

        return self._fetch_list(
            """
            SELECT DISTINCT name
            FROM authors
            """
        )

    def load_books(self):

        return self._fetch_list(
            """
            SELECT DISTINCT name
            FROM books
            """
        )

    def load_publishers(self):

        return self._fetch_list(
            """
            SELECT DISTINCT name
            FROM publishers
            """
        )

    def load_series(self):

        return self._fetch_list(
            """
            SELECT DISTINCT name
            FROM series
            """
        )

    def load_categories(self):

        return self._fetch_list(
            """
            SELECT DISTINCT name
            FROM categories
            """
        )
