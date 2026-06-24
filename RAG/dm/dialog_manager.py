from RAG.dm.schemas import (
    DialogResponse
)

from RAG.dm.utils import (
    merge_constraints,
    merge_semantic_query,
)


class DialogManager:
    def __init__(
        self,
        retrieval_service,
        interaction_service,
        state_repository
    ):
        self.retrieval_service = (
            retrieval_service
        )

        self.interaction_service = (
            interaction_service
        )

        self.state_repository = (
            state_repository
        )


    def handle(
        self,
        user_id,
        parsed
    ):
        state = (
            self.state_repository
            .get(user_id)
        )

        if parsed.intent == "greeting":
            return DialogResponse(
                action="message",
                message=(
                    "Привіт! Я допоможу підібрати українські "
                    "книги. Можете написати, що хочеться "
                    "почитати."
                )
            )

        if parsed.intent == "unknown":
            return DialogResponse(
                action="message",
                message=(
                    "Не зовсім зрозумів запит. Спробуйте "
                    "описати жанр, тему, автора або книгу, "
                    "на яку орієнтуватися."
                )
            )

        if (
            state.pending_action
            in (
                "feedback_like",
                "feedback_dislike",
            )
            and
            parsed.books
        ):
            parsed.intent = state.pending_action

        if parsed.intent == "book_query":
            return self._handle_book_query(
                parsed,
                state
            )

        if parsed.intent == "author_query":
            return self._handle_author_query(
                parsed,
                state
            )

        if parsed.intent in (
            "recommend_book",
            "similar_book",
            "clarification_answer",
        ):
            unresolved_response = (
                self._unresolved_recommendation_response(
                    parsed
                )
            )
            if unresolved_response:
                return unresolved_response

        state.current_constraints = (
            merge_constraints(
                state.current_constraints,
                parsed.structured_constraints
            )
        )
        parsed.structured_constraints = (
            state.current_constraints
        )

        state.current_semantic_query = (
            merge_semantic_query(
                state.current_semantic_query,
                parsed.semantic_query
            )
        )
        parsed.semantic_query = (
            state.current_semantic_query
        )

        # Recommendation request
        if parsed.intent in (
            "recommend_book",
            "similar_book",
            "clarification_answer",
        ):
            result = (
                self.retrieval_service
                .recommend(
                    user_id,
                    parsed
                )
            )

            if result.response_type == "clarification":
                self._set_pending(
                    state,
                    "recommend_book",
                    result.missing_fields,
                )
                self.state_repository.save(
                    state
                )
                return DialogResponse(
                    action="clarification",
                    message=result.question,
                    pending_action=state.pending_action,
                    pending_slots=state.pending_slots,
                )
            
            if result.response_type == "no_results":
                return DialogResponse(
                    action="no_results",
                    message=result.reason,
                    reason=result.reason
                )

            if result.book_ids:
                state.last_recommended_books = (
                    result.book_ids
                )
                self._set_focus_books(
                    state,
                    result.book_ids[:1]
                )

            state.recommendation_count += 1
            self._clear_pending(
                state
            )

            self.state_repository.save(
                state
            )

            return DialogResponse(
                action="recommend",
                recommendation_ids=result.book_ids,
                retrieval_type=result.retrieval_type,
                reason=result.reason,
                total_found=result.total_found,
                requested_count=result.requested_count,
                too_many_results=result.too_many_results,
            )
    
        # Like book
        if parsed.intent == (
            "feedback_like"
        ):
            book_ids = self._resolve_feedback_book_ids(
                parsed,
                state
            )
            if not book_ids:
                self._set_pending(
                    state,
                    "feedback_like",
                    ["books"],
                )
                self.state_repository.save(
                    state
                )
                return DialogResponse(
                    action="message",
                    message=
                    "Яку саме книгу ви оцінюєте?",
                    pending_action=state.pending_action,
                    pending_slots=state.pending_slots,
                )
            
            for book_id in book_ids:
                self.interaction_service.save_rating(
                    user_id,
                    book_id,
                    2
                )
            state.last_liked_book_ids = book_ids
            self._set_focus_books(
                state,
                book_ids[:1]
            )
            self._clear_pending(
                state
            )
            self.state_repository.save(
                state
            )
            return DialogResponse(
                action="message",
                message="Оцінку збережено.",
                payload={
                    "books": (
                        self.retrieval_service
                        .books_repository
                        .get_books_for_nlg(
                            book_ids
                        )
                    )
                }
            )
        
        # Dislike book
        if parsed.intent == (
            "feedback_dislike"
        ):
            book_ids = self._resolve_feedback_book_ids(
                parsed,
                state
            )
            if not book_ids:
                self._set_pending(
                    state,
                    "feedback_dislike",
                    ["books"],
                )
                self.state_repository.save(
                    state
                )
                return DialogResponse(
                    action="message",
                    message=
                    "Яку саме книгу ви оцінюєте?",
                    pending_action=state.pending_action,
                    pending_slots=state.pending_slots,
                )
            
            for book_id in book_ids:
                self.interaction_service.save_rating(
                    user_id,
                    book_id,
                    -2
                )
            self._set_focus_books(
                state,
                book_ids[:1]
            )
            self._clear_pending(
                state
            )
            self.state_repository.save(
                state
            )
            return DialogResponse(
                action="message",
                message="Оцінку збережено.",
                payload={
                    "books": (
                        self.retrieval_service
                        .books_repository
                        .get_books_for_nlg(
                            book_ids
                        )
                    )
                }
            )

        # Fallback
        return DialogResponse(
            action="message",
            message="Не вдалося обробити запит.",
        )

    def _handle_book_query(
        self,
        parsed,
        state
    ) -> DialogResponse:
        if parsed.unresolved_entities.books:
            return self._unresolved_entity_response(
                "books",
                parsed.unresolved_entities.books,
            )

        if not parsed.books:
            self._set_pending(
                state,
                "book_query",
                ["books"],
            )
            self.state_repository.save(
                state
            )
            return DialogResponse(
                action="message",
                message="Про яку саме книгу ви хочете дізнатися?",
                pending_action=state.pending_action,
                pending_slots=state.pending_slots,
            )

        book_ids = (
            self.retrieval_service
            .books_repository
            .get_book_ids_by_names(
                parsed.books
            )
        )
        books = (
            self.retrieval_service
            .books_repository
            .get_books_for_nlg(
                book_ids[:3]
            )
        )

        if not books:
            return DialogResponse(
                action="no_results",
                message="Не знайшов такої книги в базі.",
                reason="Не знайшов такої книги в базі.",
            )

        self._set_focus_books(
            state,
            book_ids[:1]
        )
        self._clear_pending(
            state
        )
        self.state_repository.save(
            state
        )

        return DialogResponse(
            action="message",
            message="Користувач запитує інформацію про книгу.",
            payload={
                "books": books
            }
        )

    def _handle_author_query(
        self,
        parsed,
        state
    ) -> DialogResponse:
        if parsed.unresolved_entities.authors:
            return self._unresolved_entity_response(
                "authors",
                parsed.unresolved_entities.authors,
            )

        authors = self._resolve_author_names(
            parsed,
            state
        )
        if not authors:
            self._set_pending(
                state,
                "author_query",
                ["authors"],
            )
            self.state_repository.save(
                state
            )
            return DialogResponse(
                action="message",
                message="Про якого саме автора ви хочете дізнатися?",
                pending_action=state.pending_action,
                pending_slots=state.pending_slots,
            )

        parsed.structured_constraints.authors = authors

        book_ids = (
            self.retrieval_service
            .books_repository
            .search_book_ids(
                parsed.structured_constraints
            )
        )
        books = (
            self.retrieval_service
            .books_repository
            .get_books(
                book_ids[:5]
            )
        )

        if not books:
            return DialogResponse(
                action="no_results",
                message="Не знайшов книг цього автора в базі.",
                reason="Не знайшов книг цього автора в базі.",
            )

        author_infos = (
            self.retrieval_service
            .books_repository
            .get_authors_by_names(
                authors
            )
        )

        state.last_mentioned_author_names = authors
        state.current_focus_author_names = authors[:1]
        if len(authors) > 1:
            self._set_pending(
                state,
                "author_query",
                ["authors"],
                {
                    "authors": authors
                }
            )
        else:
            self._clear_pending(
                state
            )
        self.state_repository.save(
            state
        )

        return DialogResponse(
            action="message",
            message=(
                "Користувач запитує інформацію про автора."
            ),
            payload={
                "authors": author_infos,
                "books": books,
            },
            pending_action=state.pending_action,
            pending_slots=state.pending_slots,
            pending_candidates=state.pending_candidates,
        )

    def _resolve_feedback_book_ids(
        self,
        parsed,
        state
    ) -> list[str]:
        if parsed.books:
            book_ids = (
                self.retrieval_service
                .books_repository
                .get_book_ids_by_names(
                    parsed.books
                )
            )
            if book_ids:
                return book_ids

        if state.current_focus_book_ids:
            return state.current_focus_book_ids

        if state.last_selected_books:
            return state.last_selected_books

        if state.last_selected_book:
            return [
                state.last_selected_book
            ]

        return []

    def _resolve_author_names(
        self,
        parsed,
        state
    ) -> list[str]:
        authors = list(
            parsed.structured_constraints.authors
        )

        if authors:
            contextual = [
                author
                for author in authors
                if author in state.current_focus_author_names
                or author in state.last_mentioned_author_names
                or author in state.pending_candidates.get(
                    "authors",
                    []
                )
            ]
            return contextual or authors

        if (
            state.pending_action == "author_query"
            and
            state.pending_candidates.get("authors")
        ):
            matches = (
                self.retrieval_service
                .books_repository
                .filter_author_names(
                    parsed.raw_utterance,
                    state.pending_candidates["authors"]
                )
            )
            if matches:
                return matches

        if (
            self._is_implicit_author_reference(
                parsed.raw_utterance
            )
            and
            state.current_focus_author_names
        ):
            return state.current_focus_author_names

        if (
            self._is_implicit_author_reference(
                parsed.raw_utterance
            )
            and
            state.current_focus_book_ids
        ):
            return (
                self.retrieval_service
                .books_repository
                .get_author_names_for_books(
                    state.current_focus_book_ids
                )
            )

        if (
            self._is_implicit_author_reference(
                parsed.raw_utterance
            )
            and
            state.last_liked_book_ids
        ):
            return (
                self.retrieval_service
                .books_repository
                .get_author_names_for_books(
                    state.last_liked_book_ids
                )
            )

        return []

    def _unresolved_entity_response(
        self,
        entity_type: str,
        values: list[str],
    ) -> DialogResponse:
        labels = {
            "authors": ("автора", "авторів"),
            "books": ("книгу", "книги"),
            "categories": ("категорію", "категорії"),
            "series": ("серію", "серії"),
            "publishers": ("видавництво", "видавництва"),
        }
        singular, plural = labels.get(
            entity_type,
            ("сутність", "сутності")
        )
        quoted_values = [
            f"«{value}»"
            for value in values
        ]
        if len(quoted_values) == 1:
            message = (
                f"Не знайшов {singular} "
                f"{quoted_values[0]} в базі."
            )
        else:
            message = (
                f"Не знайшов такі {plural}: "
                + ", ".join(quoted_values)
                + " в базі."
            )

        return DialogResponse(
            action="no_results",
            message=message,
            reason=(
                f"explicit_unresolved_{entity_type}"
            ),
            payload={
                "unresolved_entities": {
                    entity_type: values
                }
            }
        )

    def _unresolved_recommendation_response(
        self,
        parsed
    ) -> DialogResponse | None:
        if self._has_actionable_recommendation_signal(
            parsed
        ):
            return None

        unresolved = parsed.unresolved_entities

        if unresolved.authors:
            return self._unresolved_entity_response(
                "authors",
                unresolved.authors,
            )

        if unresolved.books:
            return self._unresolved_entity_response(
                "books",
                unresolved.books,
            )

        if unresolved.categories:
            return self._unresolved_entity_response(
                "categories",
                unresolved.categories,
            )

        if unresolved.series:
            return self._unresolved_entity_response(
                "series",
                unresolved.series,
            )

        if unresolved.publishers:
            return self._unresolved_entity_response(
                "publishers",
                unresolved.publishers,
            )

        return None

    def _has_actionable_recommendation_signal(
        self,
        parsed
    ) -> bool:
        constraints = parsed.structured_constraints
        semantic = parsed.semantic_query

        return any([
            parsed.books,
            constraints.authors,
            constraints.categories,
            constraints.series,
            constraints.publishers,
            constraints.languages,
            constraints.periods,
            constraints.types,
            constraints.year_from is not None,
            constraints.year_to is not None,
            constraints.pages_min is not None,
            constraints.pages_max is not None,
            semantic.free_text,
            semantic.moods,
            semantic.themes,
        ])

    def _is_implicit_author_reference(
        self,
        utterance: str
    ) -> bool:
        text = utterance.casefold()
        markers = [
            "автор",
            "автора",
            "авторка",
            "авторку",
            "його",
            "нього",
            "неї",
            "він",
            "вона",
            "доробок",
            "що ще написав",
            "що ще написала",
        ]

        return any(
            marker in text
            for marker in markers
        )

    def _set_focus_books(
        self,
        state,
        book_ids: list[str]
    ):
        state.current_focus_book_ids = book_ids
        state.last_mentioned_book_ids = book_ids
        state.current_focus_author_names = (
            self.retrieval_service
            .books_repository
            .get_author_names_for_books(
                book_ids
            )
        )

    def _set_pending(
        self,
        state,
        action: str,
        slots: list[str],
        candidates: dict[str, list[str]] | None = None,
    ):
        state.pending_action = action
        state.pending_slots = slots
        state.pending_candidates = candidates or {}

    def _clear_pending(
        self,
        state
    ):
        state.pending_action = None
        state.pending_slots = []
        state.pending_candidates = {}
