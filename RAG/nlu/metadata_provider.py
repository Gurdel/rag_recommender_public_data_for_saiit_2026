import sqlite3


class MetadataProvider:

    def __init__(self, db_path: str):

        self.db_path = db_path

    def _fetch_distinct(
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

    def get_languages(self):

        data = self._fetch_distinct(
            """
            SELECT DISTINCT language
            FROM books
            WHERE language IS NOT NULL
            """
        )
        res = set()
        for r in data:
            res.update(r.split(' , '))
        return sorted(res)

    def get_periods(self):

        return self._fetch_distinct(
            """
            SELECT DISTINCT name
            FROM periods
            """
        )

    def get_types(self):

        return self._fetch_distinct(
            """
            SELECT DISTINCT type
            FROM books
            WHERE type IS NOT NULL
            """
        )
