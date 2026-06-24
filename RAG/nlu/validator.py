import re

from RAG.nlu.schemas import ParsedUtterance


class NLUValidator:

    @staticmethod
    def _split_allowed(
        values,
        allowed_values
    ):
        allowed_set = set(
            allowed_values or []
        )
        valid = []
        invalid = []

        for value in values:
            if value in allowed_set:
                valid.append(
                    value
                )
            else:
                invalid.append(
                    value
                )

        return valid, invalid

    @staticmethod
    def _append_unique(
        target,
        values
    ):
        for value in values:
            if value not in target:
                target.append(
                    value
                )

    @staticmethod
    def preserve_unresolved_mentions(
        parsed: ParsedUtterance,
        mentions,
        candidates
    ) -> ParsedUtterance:
        NLUValidator._preserve_mentions_for_field(
            parsed.unresolved_entities.authors,
            mentions.possible_authors,
            candidates.get("authors"),
            parsed.structured_constraints.authors,
            candidates.get("_by_mention", {}).get(
                "authors",
                {}
            ),
        )
        NLUValidator._preserve_mentions_for_field(
            parsed.unresolved_entities.books,
            mentions.possible_books,
            candidates.get("books"),
            parsed.books,
            candidates.get("_by_mention", {}).get(
                "books",
                {}
            ),
        )
        NLUValidator._preserve_mentions_for_field(
            parsed.unresolved_entities.categories,
            mentions.possible_categories,
            candidates.get("categories"),
            parsed.structured_constraints.categories,
            candidates.get("_by_mention", {}).get(
                "categories",
                {}
            ),
            field_name="categories",
        )
        NLUValidator._preserve_mentions_for_field(
            parsed.unresolved_entities.series,
            mentions.possible_series,
            candidates.get("series"),
            parsed.structured_constraints.series,
            candidates.get("_by_mention", {}).get(
                "series",
                {}
            ),
        )
        NLUValidator._preserve_mentions_for_field(
            parsed.unresolved_entities.publishers,
            mentions.possible_publishers,
            candidates.get("publishers"),
            parsed.structured_constraints.publishers,
            candidates.get("_by_mention", {}).get(
                "publishers",
                {}
            ),
        )

        return parsed

    @staticmethod
    def normalize_temporal_constraints(
        parsed: ParsedUtterance
    ) -> ParsedUtterance:
        raw = parsed.raw_utterance.casefold()

        after_match = re.search(
            r"\bпісля\s+(\d{4})\b",
            raw
        )
        if after_match:
            parsed.structured_constraints.year_from = int(
                after_match.group(1)
            )

        return parsed

    @staticmethod
    def normalize_semantic_query(
        parsed: ParsedUtterance
    ) -> ParsedUtterance:
        parsed.semantic_query.themes = (
            NLUValidator._order_values_by_utterance(
                parsed.semantic_query.themes,
                parsed.raw_utterance,
            )
        )

        return parsed

    @staticmethod
    def cleanup_unresolved_entities(
        parsed: ParsedUtterance,
        candidates
    ) -> ParsedUtterance:
        category_candidates_by_mention = (
            candidates
            .get("_by_mention", {})
            .get("categories", {})
        )

        parsed.unresolved_entities.categories = [
            value
            for value in parsed.unresolved_entities.categories
            if not NLUValidator._is_non_category_constraint_phrase(
                value
            )
            and not NLUValidator._matches_semantic_theme(
                value,
                parsed.semantic_query.themes,
            )
            and not NLUValidator._mention_resolved_by_candidates(
                value,
                parsed.structured_constraints.categories,
                category_candidates_by_mention,
            )
        ]

        return parsed

    @staticmethod
    def _preserve_mentions_for_field(
        target,
        mentions,
        candidates,
        resolved_values,
        candidates_by_mention,
        field_name: str | None = None,
    ):
        candidates = candidates or []
        resolved_values = resolved_values or []
        candidates_by_mention = candidates_by_mention or {}

        for mention in mentions:
            if NLUValidator._is_generic_reference(
                mention
            ):
                continue

            if (
                field_name == "categories"
                and
                NLUValidator._is_non_category_constraint_phrase(
                    mention
                )
            ):
                continue

            if mention in candidates:
                continue

            if mention in resolved_values:
                continue

            mention_candidates = (
                candidates_by_mention.get(
                    mention,
                    []
                )
            )
            if any(
                candidate in resolved_values
                for candidate in mention_candidates
            ):
                continue

            if not mention:
                continue

            if mention not in target:
                target.append(
                    mention
                )

    @staticmethod
    def _is_generic_reference(
        mention: str
    ) -> bool:
        return mention.casefold().strip() in {
            "автор",
            "автора",
            "авторка",
            "книга",
            "книгу",
            "твір",
            "твори",
            "вона",
            "він",
            "його",
            "її",
        }

    @staticmethod
    def _is_non_category_constraint_phrase(
        mention: str
    ) -> bool:
        text = mention.casefold().strip()

        if re.search(r"\b\d{4}\b", text):
            return True

        stems = [
            "паперов",
            "електрон",
            "аудіо",
            "українськ",
            "англійськ",
            "німецьк",
            "французьк",
            "польськ",
            "російськ",
            "мов",
            "сторін",
        ]

        return any(
            stem in text
            for stem in stems
        )

    @staticmethod
    def _matches_semantic_theme(
        mention: str,
        themes
    ) -> bool:
        mention_key = NLUValidator._semantic_key(
            mention
        )

        return any(
            mention_key == NLUValidator._semantic_key(
                theme
            )
            for theme in themes
        )

    @staticmethod
    def _order_values_by_utterance(
        values,
        utterance: str
    ):
        raw = NLUValidator._normalize_text(
            utterance
        )

        return sorted(
            values,
            key=lambda value: NLUValidator._position_in_text(
                value,
                raw,
            )
        )

    @staticmethod
    def _position_in_text(
        value: str,
        normalized_text: str
    ) -> int:
        key = NLUValidator._semantic_key(
            value
        )
        words = re.findall(
            r"[\w']+",
            normalized_text
        )

        for index, word in enumerate(
            words
        ):
            if NLUValidator._semantic_key(
                word
            ) == key:
                return index

        return len(words)

    @staticmethod
    def _semantic_key(
        value: str
    ) -> str:
        text = NLUValidator._normalize_text(
            value
        )
        words = re.findall(
            r"[\w']+",
            text
        )
        if not words:
            return text

        word = words[0]
        for suffix in (
            "ою",
            "ею",
            "єю",
            "ам",
            "ям",
            "ах",
            "ях",
            "у",
            "ю",
            "а",
            "я",
            "и",
            "і",
            "ї",
            "е",
        ):
            if (
                word.endswith(suffix)
                and
                len(word) > len(suffix) + 2
            ):
                return word[:-len(suffix)]

        return word

    @staticmethod
    def _normalize_text(
        value: str
    ) -> str:
        return (
            value
            .casefold()
            .replace("’", "'")
            .replace("`", "'")
            .replace("ʼ", "'")
        )

    @staticmethod
    def _mention_resolved_by_candidates(
        mention: str,
        resolved_values,
        candidates_by_mention,
    ) -> bool:
        mention_candidates = (
            candidates_by_mention.get(
                mention,
                []
            )
        )

        return any(
            candidate in resolved_values
            for candidate in mention_candidates
        )

    @staticmethod
    def validate_allowed_values(
        parsed: ParsedUtterance,
        allowed_languages,
        allowed_periods,
        allowed_types,
        allowed_authors,
        allowed_books,
        allowed_categories,
        allowed_series,
        allowed_publishers
    ):

        parsed.structured_constraints.languages = [
            x
            for x in parsed.structured_constraints.languages
            if x in allowed_languages
        ]

        parsed.structured_constraints.periods = [
            x
            for x in parsed.structured_constraints.periods
            if x in allowed_periods
        ]

        parsed.structured_constraints.types = [
            x
            for x in parsed.structured_constraints.types
            if x in allowed_types
        ]

        (
            parsed.structured_constraints.authors,
            invalid_authors,
        ) = NLUValidator._split_allowed(
            parsed.structured_constraints.authors,
            allowed_authors,
        )
        NLUValidator._append_unique(
            parsed.unresolved_entities.authors,
            invalid_authors,
        )

        (
            parsed.structured_constraints.categories,
            invalid_categories,
        ) = NLUValidator._split_allowed(
            parsed.structured_constraints.categories,
            allowed_categories,
        )
        NLUValidator._append_unique(
            parsed.unresolved_entities.categories,
            invalid_categories,
        )

        (
            parsed.structured_constraints.series,
            invalid_series,
        ) = NLUValidator._split_allowed(
            parsed.structured_constraints.series,
            allowed_series,
        )
        NLUValidator._append_unique(
            parsed.unresolved_entities.series,
            invalid_series,
        )

        (
            parsed.structured_constraints.publishers,
            invalid_publishers,
        ) = NLUValidator._split_allowed(
            parsed.structured_constraints.publishers,
            allowed_publishers,
        )
        NLUValidator._append_unique(
            parsed.unresolved_entities.publishers,
            invalid_publishers,
        )

        (
            parsed.books,
            invalid_books,
        ) = NLUValidator._split_allowed(
            parsed.books,
            allowed_books,
        )
        NLUValidator._append_unique(
            parsed.unresolved_entities.books,
            invalid_books,
        )

        return parsed
