from pydantic import BaseModel, Field


class BookForNLG(BaseModel):

    id: str

    name: str

    description: str | None = None

    code: int | None = None

    isbn: str | None = None

    language: str | None = None

    type: str | None = None

    authors: list[str] = Field(default_factory=list)

    categories: list[str] = Field(default_factory=list)

    publisher: str | None = None

    series: str | None = None

    period: str | None = None

    year: int | None = None

    pages: int | None = None

    format: str | None = None

    images: str | None = None

    paper_type: str | None = None

    binding_type: str | None = None

    weight: int | None = None

    circulation: str | None = None


class AuthorForNLG(BaseModel):

    id: str

    name: str

    biography: str | None = None

    full_name: str | None = None

    date_of_birth: str | None = None

    additional_info: str | None = None

    items_count: int | None = None


class NLGResponse(BaseModel):

    text: str


class RecommendationContext(BaseModel):

    retrieval_type: str

    reason: str

    books: list[BookForNLG]

    total_found: int | None = None

    requested_count: int | None = None

    too_many_results: bool = False
