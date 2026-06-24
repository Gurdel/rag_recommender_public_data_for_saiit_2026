from typing import List, Optional

from pydantic import AliasChoices, BaseModel, Field, model_validator


class StructuredConstraints(BaseModel):

    authors: List[str] = Field(default_factory=list)

    categories: List[str] = Field(default_factory=list)

    series: List[str] = Field(default_factory=list)

    publishers: List[str] = Field(default_factory=list)

    languages: List[str] = Field(default_factory=list)

    periods: List[str] = Field(default_factory=list)

    types: List[str] = Field(default_factory=list)

    year_from: Optional[int] = None

    year_to: Optional[int] = None

    pages_min: Optional[int] = None

    pages_max: Optional[int] = None


class SemanticQuery(BaseModel):

    moods: List[str] = Field(default_factory=list)

    themes: List[str] = Field(default_factory=list)

    free_text: Optional[str] = None


class UnresolvedEntities(BaseModel):

    authors: List[str] = Field(default_factory=list)

    books: List[str] = Field(default_factory=list)

    categories: List[str] = Field(default_factory=list)

    series: List[str] = Field(default_factory=list)

    publishers: List[str] = Field(default_factory=list)


class ParsedUtterance(BaseModel):

    intent: str

    structured_constraints: StructuredConstraints = (
        Field(default_factory=StructuredConstraints)
    )

    semantic_query: SemanticQuery = (
        Field(default_factory=SemanticQuery)
    )

    books: List[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "books",
            "similar_to_books",
        ),
    )

    requested_count: Optional[int] = None

    unresolved_entities: UnresolvedEntities = (
        Field(default_factory=UnresolvedEntities)
    )

    raw_utterance: str

    @model_validator(mode="before")
    @classmethod
    def migrate_legacy_fields(cls, data):
        if not isinstance(data, dict):
            return data

        legacy_authors = data.pop(
            "similar_to_authors",
            None
        )
        if legacy_authors:
            constraints = data.setdefault(
                "structured_constraints",
                {}
            )
            authors = constraints.setdefault(
                "authors",
                []
            )
            constraints["authors"] = list(
                dict.fromkeys(
                    authors
                    +
                    legacy_authors
                )
            )

        return data
    
