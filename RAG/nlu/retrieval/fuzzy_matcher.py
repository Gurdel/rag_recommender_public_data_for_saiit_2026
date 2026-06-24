from rapidfuzz import fuzz
from rapidfuzz import process


class FuzzyMatcher:

    @staticmethod
    def match(
        query: str,
        choices: list[str],
        limit: int = 10,
        score_cutoff: int = 70
    ):

        if not query:
            return []

        results = process.extract(
            query=query,
            choices=choices,
            scorer=fuzz.WRatio,
            limit=limit,
            score_cutoff=score_cutoff,
        )

        return [
            match[0]
            for match in results
        ]
