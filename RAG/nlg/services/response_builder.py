from RAG.nlg.schemas import (
    AuthorForNLG,
    BookForNLG,
    RecommendationContext
)


class ResponseBuilder:

    def build_books_block(
        self,
        context: RecommendationContext
    ) -> str:

        blocks = []

        for idx, book in enumerate(
            context.books[:5],
            start=1
        ):
            blocks.append(
                self._build_book_details(
                    book,
                    idx
                )
            )

        return "\n".join(blocks)

    def build_book_details_block(
        self,
        books: list[BookForNLG]
    ) -> str:
        return "\n\n".join(
            self._build_book_details(
                book,
                idx
            )
            for idx, book in enumerate(
                books,
                start=1
            )
        )

    def build_authors_block(
        self,
        authors: list[AuthorForNLG]
    ) -> str:
        blocks = []

        for idx, author in enumerate(
            authors,
            start=1
        ):
            fields = [
                f"{idx}. {author.name}",
                f"Повне ім'я: {author.full_name or ''}",
                f"Дата народження: {author.date_of_birth or ''}",
                f"Кількість творів у базі: {author.items_count or ''}",
                f"Біографія: {author.biography or ''}",
                f"Додаткова інформація: {author.additional_info or ''}",
            ]
            blocks.append(
                "\n".join(fields)
            )

        return "\n\n".join(blocks)

    def _build_book_details(
        self,
        book: BookForNLG,
        idx: int
    ) -> str:
        fields = [
            f"{idx}. {book.name}",
            f"Автори: {', '.join(book.authors)}",
            f"Категорії: {', '.join(book.categories)}",
            f"Опис: {book.description or ''}",
            f"Тип: {book.type or ''}",
            f"Мова: {book.language or ''}",
            f"Видавництво: {book.publisher or ''}",
            f"Серія: {book.series or ''}",
            f"Період: {book.period or ''}",
            f"Рік: {book.year or ''}",
            f"Сторінок: {book.pages or ''}",
            f"ISBN: {book.isbn or ''}",
            f"Код: {book.code or ''}",
            f"Формат: {book.format or ''}",
            f"Тип паперу: {book.paper_type or ''}",
            f"Тип палітурки: {book.binding_type or ''}",
            f"Вага: {book.weight or ''}",
            f"Тираж: {book.circulation or ''}",
            f"Зображення: {book.images or ''}",
        ]

        return "\n".join(fields)
