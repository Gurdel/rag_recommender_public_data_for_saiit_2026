from RAG.nlu.schemas import (
    StructuredConstraints,
    SemanticQuery,
)


def merge_constraints(
    old: StructuredConstraints,
    new: StructuredConstraints
):
    merged = old.model_copy(
        deep=True
    )

    if new.authors:
        merged.authors = (
            new.authors
        )

    if new.categories:
        merged.categories = (
            new.categories
        )

    if new.series:
        merged.series = (
            new.series
        )

    if new.publishers:
        merged.publishers = (
            new.publishers
        )

    if new.languages:
        merged.languages = (
            new.languages
        )

    if new.periods:
        merged.periods = (
            new.periods
        )

    if new.types:
        merged.types = (
            new.types
        )

    if new.year_from is not None:
        merged.year_from = (
            new.year_from
        )

    if new.year_to is not None:
        merged.year_to = (
            new.year_to
        )

    if new.pages_min is not None:
        merged.pages_min = (
            new.pages_min
        )

    if new.pages_max is not None:
        merged.pages_max = (
            new.pages_max
        )

    return merged


def merge_semantic_query(
    old: SemanticQuery,
    new: SemanticQuery,
):
    merged = old.model_copy(
        deep=True
    )
    if new.free_text:

        if merged.free_text:

            merged.free_text += (
                " "
                + new.free_text
            )

        else:

            merged.free_text = (
                new.free_text
            )
    merged.moods = list(
        set(
            merged.moods
            +
            new.moods
        )
    )

    merged.themes = list(
        set(
            merged.themes
            +
            new.themes
        )
    )
    return merged
