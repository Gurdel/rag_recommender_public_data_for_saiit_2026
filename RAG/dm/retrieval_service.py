from RAG.dm.schemas import (
    RetrievalResult,
)

from RAG.dm.repositories.books_repository import (
    BooksRepository,
)

from RAG.dm.repositories.chroma_repository import (
    ChromaRepository,
)

from RAG.dm.ranking_service import (
    RankingService,
)

from RAG.dm.clarification_service import (
    ClarificationService,
)

from RAG.nlu.schemas import ParsedUtterance


class RetrievalService:

    MAX_SQL_RESULTS = 100

    DEFAULT_RECOMMENDATION_COUNT = 3

    def __init__(
        self,
        books_repository: BooksRepository,
        chroma_repository: ChromaRepository,
        ranking_service: RankingService,
        clarification_service: ClarificationService,
    ):

        self.books_repository = (
            books_repository
        )

        self.chroma_repository = (
            chroma_repository
        )

        self.ranking_service = (
            ranking_service
        )

        self.clarification_service = (
            clarification_service
        )

    def recommend(
        self,
        user_id: int,
        parsed: ParsedUtterance
    ) -> RetrievalResult:

        has_constraints = any([
            parsed.structured_constraints.authors,
            parsed.structured_constraints.categories,
            parsed.structured_constraints.series,
            parsed.structured_constraints.publishers,
            parsed.structured_constraints.languages,
            parsed.structured_constraints.periods,
            parsed.structured_constraints.types,
            parsed.structured_constraints.year_from,
            parsed.structured_constraints.year_to,
            parsed.structured_constraints.pages_min,
            parsed.structured_constraints.pages_max
        ])

        semantic_text = self._semantic_text(
            parsed
        )

        has_semantic = bool(
            semantic_text
        )

        # -------------------------
        # similar book
        # -------------------------

        if (
            parsed.intent == "similar_book"
            and
            parsed.books
        ):

            return self._recommend_similar_books(
                parsed,
                self._requested_count(
                    parsed
                )
            )

        # -------------------------
        # similar author
        # -------------------------

        if (
            parsed.intent == "similar_book"
            and
            parsed.structured_constraints.authors
        ):

            return self._recommend_similar_author(
                parsed
            )

        # -------------------------
        # hybrid
        # -------------------------

        if (
            has_constraints
            and
            has_semantic
        ):

            return self._hybrid_search(
                user_id,
                parsed
            )

        # -------------------------
        # sql
        # -------------------------

        if has_constraints:

            return self._sql_search(
                user_id,
                parsed
            )

        # -------------------------
        # semantic
        # -------------------------

        if has_semantic:

            return self._semantic_search(
                parsed,
                self._requested_count(
                    parsed
                )
            )

        # -------------------------
        # profile
        # -------------------------

        return self._profile_recommendation(
            user_id,
            self._requested_count(
                parsed
            )
        )
    

    def _sql_search(
        self,
        user_id,
        parsed
    ):
        limit = self._requested_count(
            parsed
        )

        book_ids = (
            self.books_repository
            .search_book_ids(
                parsed.structured_constraints
            )
        )

        if not book_ids:
            return (
                self.clarification_service
                .no_results()
            )

        if len(book_ids) > limit:
            return self._rank_by_profile(
                user_id,
                book_ids,
                limit,
                total_found=len(book_ids),
                reason="too_many_structured_constraints",
                too_many_results=True,
                retrieval_type="hybrid",
            )

        return RetrievalResult(
            book_ids=book_ids[:limit],
            retrieval_type="sql",
            reason="structured_constraints",
            total_found=len(book_ids),
            requested_count=limit,
            too_many_results=False,
        )
    

    def _semantic_search(
        self,
        parsed,
        limit
    ):
        semantic_text = self._semantic_text(
            parsed
        )

        results = (
            self.chroma_repository
            .semantic_search(
                semantic_text,
                top_k=limit
            )
        )

        return RetrievalResult(
            book_ids=[
                r["id"]
                for r in results
            ],
            retrieval_type="semantic",
            reason="semantic_query",
            total_found=len(results),
            requested_count=limit,
        )


    def _hybrid_search(
        self,
        user_id,
        parsed
    ):
        semantic_text = self._semantic_text(
            parsed
        )
        limit = self._requested_count(
            parsed
        )

        sql_book_ids = (
            self.books_repository
            .search_book_ids(
                parsed.structured_constraints
            )
        )

        if not sql_book_ids:
            # return RetrievalResult(
            #     book_ids=[],
            #     retrieval_type="hybrid",
            #     reason="no_books_found"
            # )
            return (
                self.clarification_service
                .no_results()
            )

        semantic_results = (
            self.chroma_repository
            .semantic_search(
                semantic_text,
                candidate_book_ids=sql_book_ids,
                top_k=limit
            )
        )

        if semantic_results:

            return RetrievalResult(
                book_ids=[
                    x["id"]
                    for x in semantic_results
                ],
                retrieval_type="hybrid",
                reason=(
                    "too_many_semantic_and_constraints"
                    if len(sql_book_ids) > limit
                    else
                    "semantic_and_constraints"
                ),
                total_found=len(sql_book_ids),
                requested_count=limit,
                too_many_results=(
                    len(sql_book_ids) > limit
                ),
            )

        return self._rank_by_profile(
            user_id,
            sql_book_ids,
            limit,
            total_found=len(sql_book_ids),
            reason=(
                "too_many_structured_constraints"
                if len(sql_book_ids) > limit
                else
                "structured_constraints"
            ),
            too_many_results=(
                len(sql_book_ids) > limit
            ),
            retrieval_type="hybrid",
        )


    def _rank_by_profile(
        self,
        user_id,
        candidate_book_ids,
        limit,
        total_found=None,
        reason="profile_ranking",
        too_many_results=False,
        retrieval_type="profile",
    ):

        user_embedding = (
            self.chroma_repository
            .get_user_embedding(
                user_id
            )
        )
        if user_embedding is None:
            return RetrievalResult(
                book_ids=candidate_book_ids[:limit],
                retrieval_type=retrieval_type,
                reason=reason,
                total_found=(
                    total_found
                    if total_found is not None
                    else
                    len(candidate_book_ids)
                ),
                requested_count=limit,
                too_many_results=too_many_results,
            )

        embeddings = (
            self.chroma_repository
            .get_book_embeddings(
                candidate_book_ids
            )
        )

        ranked = (
            self.ranking_service
            .rank_books(
                user_embedding,
                embeddings
            )
        )

        return RetrievalResult(
            book_ids=[
                book_id
                for book_id, _
                in ranked[:limit]
            ],
            retrieval_type=retrieval_type,
            reason=reason,
            total_found=(
                total_found
                if total_found is not None
                else
                len(candidate_book_ids)
            ),
            requested_count=limit,
            too_many_results=too_many_results,
        )


    def _profile_recommendation(
        self,
        user_id,
        limit
    ):
        user_embedding = (
            self.chroma_repository
            .get_user_embedding(
                user_id
            )
        )
        if user_embedding is None:
            return RetrievalResult(
                book_ids=[],
                retrieval_type="profile",
                reason="no_profile_embedding_dimension",
                total_found=0,
                requested_count=limit,
            )

        result = (
            self.chroma_repository
            .books_collection
            .query(
                query_embeddings=[
                    user_embedding
                ],
                n_results=limit
            )
        )

        return RetrievalResult(
            book_ids=result["ids"][0],
            retrieval_type="profile",
            reason="user_embedding",
            total_found=len(result["ids"][0]),
            requested_count=limit,
        )


    def _recommend_similar_books(
        self,
        parsed,
        limit
    ):

        book_name = (
            parsed.books[0]
        )

        book_id = (
            self.books_repository
            .get_book_id_by_name(
                book_name
            )
        )

        if not book_id:
            # return RetrievalResult(
            #     book_ids=[],
            #     retrieval_type="similar_book",
            #     reason="book_not_found"
            # )
            return (
                self.clarification_service
                .no_results()
            )

        similar_books = (
            self.chroma_repository
            .recommend_similar_book(
                book_id,
                top_k=limit
            )
        )

        return RetrievalResult(
            book_ids=[
                x["id"]
                for x in similar_books
            ],
            retrieval_type="similar_book",
            reason=book_name,
            total_found=len(similar_books),
            requested_count=limit,
        )


    def _recommend_similar_author(
        self,
        parsed
    ):
        limit = self._requested_count(
            parsed
        )

        author = (
            parsed.structured_constraints.authors[0]
        )

        constraints = (
            parsed.structured_constraints
        )

        constraints.authors = [
            author
        ]

        ids = (
            self.books_repository
            .search_book_ids(
                constraints
            )
        )

        return RetrievalResult(
            book_ids=ids[:limit],
            retrieval_type="author",
            reason=author,
            total_found=len(ids),
            requested_count=limit,
            too_many_results=(
                len(ids) > limit
            ),
        )

    def _requested_count(
        self,
        parsed: ParsedUtterance
    ) -> int:
        if parsed.requested_count is None:
            return self.DEFAULT_RECOMMENDATION_COUNT

        return max(
            1,
            min(
                parsed.requested_count,
                20
            )
        )


    def _semantic_text(
        self,
        parsed: ParsedUtterance
    ) -> str:
        parts = []

        if parsed.semantic_query.free_text:
            parts.append(
                parsed.semantic_query.free_text
            )

        parts.extend(
            parsed.semantic_query.moods
        )
        parts.extend(
            parsed.semantic_query.themes
        )

        return " ".join(parts).strip()
