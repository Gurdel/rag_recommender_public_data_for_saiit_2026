from typing import List

from pydantic import BaseModel
from pydantic import Field


class MentionExtraction(BaseModel):

    possible_books: List[str] = (
        Field(default_factory=list)
    )

    possible_authors: List[str] = (
        Field(default_factory=list)
    )

    possible_publishers: List[str] = (
        Field(default_factory=list)
    )

    possible_series: List[str] = (
        Field(default_factory=list)
    )

    possible_categories: List[str] = (
        Field(default_factory=list)
    )
