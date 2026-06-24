from typing import Any, Literal

from pydantic import BaseModel, Field

from typing import Optional

from RAG.nlu.schemas import ParsedUtterance


class RecommendedBook(BaseModel):

    id: str

    name: str

    score: float


class RecommendationResult(BaseModel):

    books: list[RecommendedBook]

    retrieval_type: Literal[
        "sql",
        "semantic",
        "hybrid",
        "profile"
    ]

    reason: str


# class RetrievalResult(BaseModel):

#     book_ids: list[str]

#     retrieval_type: str

#     reason: str

class RetrievalResponse(
    BaseModel
):
    pass


class RetrievalResult(
    RetrievalResponse
):

    response_type: Literal[
        "recommendation"
    ] = "recommendation"

    book_ids: list[str]

    retrieval_type: str

    reason: str

    total_found: int | None = None

    requested_count: int | None = None

    too_many_results: bool = False


class ClarificationResult(
    RetrievalResponse
):

    response_type: Literal[
        "clarification"
    ] = "clarification"

    question: str

    missing_fields: list[str]


class NoResultsResult(
    RetrievalResponse
):

    response_type: Literal[
        "no_results"
    ] = "no_results"

    reason: str


class DialogResponse(
    BaseModel
):

    action: str

    message: str | None = None

    recommendation_ids: (
        list[str]
    ) = Field(default_factory=list)

    retrieval_type: str | None = None

    reason: str | None = None

    total_found: int | None = None

    requested_count: int | None = None

    too_many_results: bool = False

    payload: dict[str, Any] = Field(default_factory=dict)

    pending_action: str | None = None

    pending_slots: list[str] = Field(default_factory=list)

    pending_candidates: dict[str, list[str]] = Field(default_factory=dict)


class ClarificationRequest(BaseModel):

    question: str

    missing_fields: list[str]
