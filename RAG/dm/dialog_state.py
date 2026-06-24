from pydantic import BaseModel, Field

from RAG.nlu.schemas import (
    StructuredConstraints,
    SemanticQuery,
)


class DialogState(BaseModel):

    user_id: int

    current_constraints: (
        StructuredConstraints
    ) = Field(default_factory=StructuredConstraints)

    current_semantic_query: (
        SemanticQuery
    ) = Field(default_factory=SemanticQuery)

    last_recommended_books: (
        list[str]
    ) = Field(default_factory=list)

    last_selected_books: (
        list[str]
    ) = Field(default_factory=list)

    last_selected_book: str | None = None

    current_focus_book_ids: list[str] = Field(default_factory=list)

    current_focus_author_names: list[str] = Field(default_factory=list)

    last_mentioned_book_ids: list[str] = Field(default_factory=list)

    last_mentioned_author_names: list[str] = Field(default_factory=list)

    last_liked_book_ids: list[str] = Field(default_factory=list)

    pending_action: str | None = None

    pending_slots: list[str] = Field(default_factory=list)

    pending_candidates: dict[str, list[str]] = Field(default_factory=dict)

    recommendation_count: int = 0




