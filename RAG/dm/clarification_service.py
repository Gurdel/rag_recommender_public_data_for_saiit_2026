from RAG.dm.schemas import (
    ClarificationResult,
    NoResultsResult,
)


class ClarificationService:
    # Too many books
    def too_many_results(
        self,
        count: int
    ):
        if count > 1000:

            return ClarificationResult(
                question=(
                    "Можете уточнити жанр або тему книги?"
                ),
                missing_fields=[
                    "categories",
                    "themes",
                ]
            )
        if count > 300:

            return ClarificationResult(
                question=(
                    "Вас цікавить сучасна чи класична література?"
                ),
                missing_fields=[
                    "periods",
                ]
            )
        return None

    # No books
    def no_results(
        self
    ):
        return NoResultsResult(
            reason=(
                "За такими умовами книги не знайдено. "
                "Можливо змінимо критерії пошуку?"
            )
        )
