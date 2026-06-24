from RAG.nlg.schemas import (
    AuthorForNLG,
    BookForNLG,
    RecommendationContext,
    NLGResponse,
)
from RAG.dm.schemas import DialogResponse

from RAG.nlg.services.response_builder import (
    ResponseBuilder,
)

from RAG.nlg.services.explanation_service import (
    ExplanationService,
)


class NLGService:

    def __init__(
        self,
        llm_client,
        prompt_repository
    ):

        self.llm_client = llm_client

        self.prompt_repository = (
            prompt_repository
        )

        self.response_builder = (
            ResponseBuilder()
        )

        self.explanation_service = (
            ExplanationService()
        )

    def generate(
        self,
        dialog_response: DialogResponse,
        user_utterance: str | None = None,
        recommendation_books: list[BookForNLG] | None = None,
    ) -> NLGResponse:
        if dialog_response.action == "recommend":
            if not recommendation_books:
                return self.generate_no_results(
                    dialog_response.reason,
                    user_utterance=user_utterance,
                )

            return self.generate_recommendation(
                RecommendationContext(
                    retrieval_type=(
                        dialog_response.retrieval_type
                        or
                        "unknown"
                    ),
                    reason=(
                        dialog_response.reason
                        or
                        ""
                    ),
                    books=recommendation_books,
                    total_found=dialog_response.total_found,
                    requested_count=dialog_response.requested_count,
                    too_many_results=dialog_response.too_many_results,
                ),
                user_utterance=user_utterance,
            )

        if dialog_response.action == "clarification":
            return self.generate_clarification(
                dialog_response.message
                or
                "",
                user_utterance=user_utterance,
                pending_action=dialog_response.pending_action,
                pending_slots=dialog_response.pending_slots,
                pending_candidates=dialog_response.pending_candidates,
            )

        if dialog_response.action == "no_results":
            return self.generate_no_results(
                dialog_response.message
                or
                dialog_response.reason,
                user_utterance=user_utterance,
            )

        return self.generate_message(
            dialog_response,
            user_utterance=user_utterance,
        )


    # Recommendation
    def generate_recommendation(
        self,
        context: RecommendationContext,
        user_utterance: str | None = None,
    ) -> NLGResponse:

        system_prompt = (
            self.prompt_repository.load(
                "recommendation.txt"
            )
        )

        books_block = (
            self.response_builder
            .build_books_block(
                context
            )
        )

        explanation = (
            self.explanation_service
            .build_reason(
                context.retrieval_type,
                context.reason
            )
        )
        result_note = self._build_result_note(
            context
        )

        user_prompt = f"""
Запит користувача:
{user_utterance or ""}

Інформація про кількість результатів:
{result_note}

Причина рекомендації:

{explanation}

Книги:

{books_block}
"""

        text = (
            self.llm_client.generate(
                system_prompt,
                user_prompt
            )
        )

        return NLGResponse(
            text=text
        )

    def _build_result_note(
        self,
        context: RecommendationContext
    ) -> str:
        if (
            context.too_many_results
            and
            context.total_found is not None
        ):
            return (
                f"Знайдено {context.total_found} книг. "
                f"Покажи {len(context.books)} найбільш релевантні."
            )

        if context.total_found is not None:
            return (
                f"Знайдено {context.total_found} книг. "
                f"Покажи {len(context.books)}."
            )

        return ""


    # Clarification
    def generate_clarification(
        self,
        question: str,
        user_utterance: str | None = None,
        pending_action: str | None = None,
        pending_slots: list[str] | None = None,
        pending_candidates: dict[str, list[str]] | None = None,
    ) -> NLGResponse:
        system_prompt = (
            self.prompt_repository.load(
                "clarification.txt"
            )
        )

        user_prompt = f"""
Запит користувача:
{user_utterance or ""}

Уточнення від dialog manager:
{question}

Pending action:
{pending_action or ""}

Pending slots:
{pending_slots or []}

Pending candidates:
{pending_candidates or {}}
"""

        text = (
            self.llm_client.generate(
                system_prompt,
                user_prompt
            )
        )

        return NLGResponse(
            text=text
        )


    # No results
    def generate_no_results(
        self,
        reason: str | None = None,
        user_utterance: str | None = None,
    ) -> NLGResponse:
        system_prompt = (
            self.prompt_repository.load(
                "no_results.txt"
            )
        )

        user_prompt = f"""
Запит користувача:
{user_utterance or ""}

Причина:
{reason or "Книг не знайдено."}
"""

        text = (
            self.llm_client.generate(
                system_prompt,
                user_prompt
            )
        )

        return NLGResponse(
            text=text
        )

    def generate_message(
        self,
        dialog_response: DialogResponse,
        user_utterance: str | None = None,
    ) -> NLGResponse:
        system_prompt = (
            self.prompt_repository.load(
                "message.txt"
            )
        )

        books = [
            BookForNLG(**book)
            for book in dialog_response.payload.get(
                "books",
                []
            )
        ]
        authors = [
            AuthorForNLG(**author)
            for author in dialog_response.payload.get(
                "authors",
                []
            )
        ]

        books_block = (
            self.response_builder
            .build_book_details_block(
                books
            )
            if books
            else
            ""
        )
        authors_block = (
            self.response_builder
            .build_authors_block(
                authors
            )
            if authors
            else
            ""
        )

        user_prompt = f"""
Запит користувача:
{user_utterance or ""}

Повідомлення від dialog manager:
{dialog_response.message or ""}

Pending action:
{dialog_response.pending_action or ""}

Pending slots:
{dialog_response.pending_slots}

Pending candidates:
{dialog_response.pending_candidates}

Автори:
{authors_block}

Книги:
{books_block}
"""

        text = (
            self.llm_client.generate(
                system_prompt,
                user_prompt
            )
        )

        return NLGResponse(
            text=text
        )
