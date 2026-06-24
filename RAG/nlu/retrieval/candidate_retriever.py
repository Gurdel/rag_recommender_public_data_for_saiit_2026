from RAG.nlu.retrieval.metadata_loader import (
    MetadataLoader
)

from RAG.nlu.retrieval.fuzzy_matcher import (
    FuzzyMatcher
)


class CandidateRetriever:

    def __init__(
        self,
        db_path: str
    ):

        self.loader = MetadataLoader(
            db_path
        )

        self.authors = (
            self.loader.load_authors()
        )

        self.books = (
            self.loader.load_books()
        )

        self.publishers = (
            self.loader.load_publishers()
        )

        self.series = (
            self.loader.load_series()
        )

        self.categories = (
            self.loader.load_categories()
        )

    def retrieve(
        self,
        mentions
    ):

        author_candidates = []
        author_candidates_by_mention = {}
        for mention in mentions.possible_authors:
            matches = FuzzyMatcher.match(
                mention,
                self.authors
            )
            author_candidates_by_mention[mention] = matches
            author_candidates.extend(
                matches
            )

        book_candidates = []
        book_candidates_by_mention = {}
        for mention in mentions.possible_books:
            matches = FuzzyMatcher.match(
                mention,
                self.books
            )
            book_candidates_by_mention[mention] = matches
            book_candidates.extend(
                matches
            )

        publisher_candidates = []
        publisher_candidates_by_mention = {}
        for mention in mentions.possible_publishers:
            matches = FuzzyMatcher.match(
                mention,
                self.publishers
            )
            publisher_candidates_by_mention[mention] = matches
            publisher_candidates.extend(
                matches
            )

        series_candidates = []
        series_candidates_by_mention = {}
        for mention in mentions.possible_series:
            matches = FuzzyMatcher.match(
                mention,
                self.series
            )
            series_candidates_by_mention[mention] = matches
            series_candidates.extend(
                matches
            )

        category_candidates = []
        category_candidates_by_mention = {}
        for mention in mentions.possible_categories:
            matches = FuzzyMatcher.match(
                mention,
                self.categories
            )
            category_candidates_by_mention[mention] = matches
            category_candidates.extend(
                matches
            )

        # print('DEBUG: CandidateRetriever:', {
        #     "authors": list(set(author_candidates)),
        #     "books": list(set(book_candidates)),
        #     "publishers": list(set(publisher_candidates)),
        #     "series": list(set(series_candidates)),
        #     "categories": list(set(category_candidates)),
        # })

        return {
            "authors": list(set(author_candidates)),
            "books": list(set(book_candidates)),
            "publishers": list(set(publisher_candidates)),
            "series": list(set(series_candidates)),
            "categories": list(set(category_candidates)),
            "_by_mention": {
                "authors": author_candidates_by_mention,
                "books": book_candidates_by_mention,
                "publishers": publisher_candidates_by_mention,
                "series": series_candidates_by_mention,
                "categories": category_candidates_by_mention,
            }
        }
