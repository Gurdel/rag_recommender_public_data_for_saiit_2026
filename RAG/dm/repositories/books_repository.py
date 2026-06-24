import sqlite3

from RAG.dm.sql_builder import SQLQueryBuilder

from RAG.nlu.schemas import (
    StructuredConstraints
)


class BooksRepository:

    def __init__(
        self,
        db_path: str
    ):

        self.db_path = db_path


    def search_book_ids(
        self,
        constraints: StructuredConstraints
    ) -> list[str]:

        query, params = (
            SQLQueryBuilder.build(
                constraints
            )
        )

        conn = sqlite3.connect(
            self.db_path
        )

        rows = conn.execute(
            query,
            params
        ).fetchall()

        conn.close()

        return [
            row[0]
            for row in rows
        ]


    def get_books(
        self,
        book_ids: list[str]
    ):

        if not book_ids:
            return []

        placeholders = ",".join(
            ["?"] * len(book_ids)
        )

        query = f"""
        SELECT
            b.id,
            b.name,
            b.description,
            b.code,
            b.isbn,
            b.language,
            b.type,
            b.year,
            b.pages,
            b.format,
            b.images,
            b.paper_type,
            b.binding_type,
            b.weight,
            b.circulation,
            p.name AS publisher,
            pr.name AS period,
            s.name AS series
        FROM books b
        LEFT JOIN publishers p
            ON p.id = b.publisher_id
        LEFT JOIN periods pr
            ON pr.id = b.period_id
        LEFT JOIN series s
            ON s.id = b.series_id
        WHERE b.id IN ({placeholders})
        """

        conn = sqlite3.connect(
            self.db_path
        )

        rows = conn.execute(
            query,
            book_ids
        ).fetchall()

        conn.close()

        books = []

        for row in rows:

            books.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "code": row[3],
                    "isbn": row[4],
                    "language": row[5],
                    "type": row[6],
                    "year": row[7],
                    "pages": row[8],
                    "format": row[9],
                    "images": row[10],
                    "paper_type": row[11],
                    "binding_type": row[12],
                    "weight": row[13],
                    "circulation": row[14],
                    "publisher": row[15],
                    "period": row[16],
                    "series": row[17],
                }
            )

        by_id = {
            book["id"]: book
            for book in books
        }

        return [
            by_id[book_id]
            for book_id in book_ids
            if book_id in by_id
        ]


    def get_books_for_nlg(
        self,
        book_ids: list[str]
    ):
        books = self.get_books(
            book_ids
        )

        for book in books:
            book["authors"] = (
                self.get_book_authors(
                    book["id"]
                )
            )
            book["categories"] = (
                self.get_book_categories(
                    book["id"]
                )
            )

        return books


    def get_book_ids_by_names(
        self,
        book_names: list[str]
    ) -> list[str]:
        book_ids = []

        for book_name in book_names:
            book_id = self.get_book_id_by_name(
                book_name
            )
            if book_id:
                book_ids.append(
                    book_id
                )

        return book_ids


    def get_book_authors(
        self,
        book_id: str
    ) -> list[str]:

        conn = sqlite3.connect(
            self.db_path
        )

        rows = conn.execute(
            """
            SELECT a.name

            FROM authors a

            JOIN book_authors ba
                ON ba.author_id = a.id

            WHERE ba.book_id = ?
            """,
            (book_id,)
        ).fetchall()

        conn.close()

        return [
            row[0]
            for row in rows
        ]


    def get_book_categories(
        self,
        book_id: str
    ) -> list[str]:

        conn = sqlite3.connect(
            self.db_path
        )

        rows = conn.execute(
            """
            SELECT c.name

            FROM categories c

            JOIN book_categories bc
                ON bc.category_id = c.id

            WHERE bc.book_id = ?
            """,
            (book_id,)
        ).fetchall()

        conn.close()

        return [
            row[0]
            for row in rows
        ]


    def get_authors_by_names(
        self,
        author_names: list[str]
    ):
        if not author_names:
            return []

        placeholders = ",".join(
            ["?"] * len(author_names)
        )

        conn = sqlite3.connect(
            self.db_path
        )

        rows = conn.execute(
            f"""
            SELECT
                id,
                name,
                biography,
                full_name,
                date_of_birth,
                additional_info,
                items_count
            FROM authors
            WHERE name IN ({placeholders})
            """,
            author_names
        ).fetchall()

        conn.close()

        authors = []
        for row in rows:
            authors.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "biography": row[2],
                    "full_name": row[3],
                    "date_of_birth": row[4],
                    "additional_info": row[5],
                    "items_count": row[6],
                }
            )

        by_name = {
            author["name"]: author
            for author in authors
        }

        return [
            by_name[name]
            for name in author_names
            if name in by_name
        ]


    def get_author_names_for_books(
        self,
        book_ids: list[str]
    ) -> list[str]:
        names = []

        for book_id in book_ids:
            names.extend(
                self.get_book_authors(
                    book_id
                )
            )

        return list(
            dict.fromkeys(
                names
            )
        )


    def filter_author_names(
        self,
        query: str,
        author_names: list[str]
    ) -> list[str]:
        normalized_query = query.casefold()

        matches = [
            name
            for name in author_names
            if normalized_query in name.casefold()
        ]

        if matches:
            return matches

        tokens = [
            token
            for token in normalized_query.split()
            if token
        ]

        return [
            name
            for name in author_names
            if all(
                token in name.casefold()
                for token in tokens
            )
        ]


    # TODO: do we need this function since search_book_ids() should cover the same logic?
    # TODO: if yes, modify WHERE statement since LOWER is not working
    def get_book_id_by_name(
        self,
        book_name: str
    ) -> str | None:

        conn = sqlite3.connect(
            self.db_path
        )

        row = conn.execute(
            """
            SELECT id

            FROM books

            WHERE name = ?
                OR name = ? COLLATE NOCASE

            LIMIT 1
            """,
            (
                book_name,
                book_name,
            )
        ).fetchone()

        conn.close()

        if row:
            return row[0]

        return None
