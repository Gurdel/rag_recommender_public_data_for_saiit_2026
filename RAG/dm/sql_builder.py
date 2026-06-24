from RAG.nlu.schemas import StructuredConstraints


class SQLQueryBuilder:

    @staticmethod
    def build(
        constraints: StructuredConstraints
    ) -> tuple[str, list]:

        query = """
        SELECT DISTINCT b.id
        FROM books b
        """

        joins = []
        where = []
        params = []

        # ---------- AUTHORS ----------

        if constraints.authors:

            joins.extend([
                """ JOIN book_authors ba ON ba.book_id = b.id """,
                """ JOIN authors a ON a.id = ba.author_id """
            ])

            placeholders = ",".join(
                ["?"] * len(constraints.authors)
            )

            where.append(
                f"a.name IN ({placeholders})"
            )

            params.extend(
                constraints.authors
            )

        # ---------- CATEGORIES ----------

        if constraints.categories:

            joins.extend([
                """ JOIN book_categories bc ON bc.book_id = b.id """,
                """ JOIN categories c ON c.id = bc.category_id """
            ])

            placeholders = ",".join(
                ["?"] * len(constraints.categories)
            )

            where.append(
                f"c.name IN ({placeholders})"
            )

            params.extend(
                constraints.categories
            )

        # ---------- SERIES ----------

        if constraints.series:

            placeholders = ",".join(
                ["?"] * len(constraints.series)
            )

            joins.append(
                """ JOIN series s ON s.id = b.series_id """
            )

            where.append(
                f"s.name IN ({placeholders})"
            )

            params.extend(
                constraints.series
            )

        # ---------- PUBLISHERS ----------

        if constraints.publishers:

            placeholders = ",".join(
                ["?"] * len(constraints.publishers)
            )

            joins.append(
                """ JOIN publishers p ON p.id = b.publisher_id """
            )

            where.append(
                f"p.name IN ({placeholders})"
            )

            params.extend(
                constraints.publishers
            )

        # ---------- PERIODS ----------

        if constraints.periods:

            placeholders = ",".join(
                ["?"] * len(constraints.periods)
            )

            joins.append(
                """ JOIN periods pr ON pr.id = b.period_id """
            )

            where.append(
                f"pr.name IN ({placeholders})"
            )

            params.extend(
                constraints.periods
            )

        # ---------- LANGUAGES ----------

        if constraints.languages:

            placeholders = ",".join(
                ["?"] * len(constraints.languages)
            )

            lang_conds = [
                f"b.language LIKE ?"
                for _ in constraints.languages
            ]

            where.append(
                '(' + " OR ".join(lang_conds) + ')'
            )

            params.extend(
                ['%' + lang + '%' for lang in constraints.languages]
            )

        # ---------- TYPES ----------

        if constraints.types:

            placeholders = ",".join(
                ["?"] * len(constraints.types)
            )

            where.append(
                f"b.type IN ({placeholders})"
            )

            params.extend(
                constraints.types
            )

        # ---------- YEAR ----------

        if constraints.year_from is not None:

            where.append(
                "b.year >= ?"
            )

            params.append(
                constraints.year_from
            )

        if constraints.year_to is not None:

            where.append(
                "b.year <= ?"
            )

            params.append(
                constraints.year_to
            )

        # ---------- PAGES ----------

        if constraints.pages_min is not None:

            where.append(
                "b.pages >= ?"
            )

            params.append(
                constraints.pages_min
            )

        if constraints.pages_max is not None:

            where.append(
                "b.pages <= ?"
            )

            params.append(
                constraints.pages_max
            )

        query += "\n".join(joins)

        if where:

            query += "\nWHERE\n"

            query += "\nAND\n".join(where)

        print('DEBUG: SQLQueryBuilder: query =', query, '\n params =', params)
        return query, params
