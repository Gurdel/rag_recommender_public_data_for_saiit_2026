import json

from openai import OpenAI

from RAG.config.settings import settings

from RAG.nlu.schemas import ParsedUtterance

from RAG.nlu.prompts import build_system_prompt

from RAG.nlu.metadata_provider import MetadataProvider

from RAG.nlu.retrieval.candidate_retriever import (
    CandidateRetriever
)

from RAG.nlu.validator import NLUValidator

from RAG.nlu.entity_extraction.mention_extractor import MentionExtractor


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


class NLUParser:

    def __init__(self):

        self.metadata = MetadataProvider(settings.BOOKS_DB_PATH)
        self.languages = self.metadata.get_languages()
        self.periods = self.metadata.get_periods()
        self.types = self.metadata.get_types()

        self.candidates = CandidateRetriever(
            settings.BOOKS_DB_PATH
        )

        self.mention_extractor = MentionExtractor()

    def parse(
        self,
        utterance: str,
        dialog_context: dict | None = None,
    ) -> ParsedUtterance:
        print('|ps|')#, end='')
        possible_mentions = self.mention_extractor.extract(utterance)
        print('|em|')#, end='')

        candidates = self.candidates.retrieve(possible_mentions)
        print('|gc|')#, end='')

        system_prompt = build_system_prompt(
            languages=self.languages,
            periods=self.periods,
            types=self.types,
            author_candidates=candidates.get("authors"),
            book_candidates=candidates.get("books"),
            category_candidates=candidates.get("categories"),
            series_candidates=candidates.get("series"),
            publisher_candidates=candidates.get("publishers"),
            dialog_context=dialog_context,
        )
        print('|sp|')#, end='')

        # print('DEBUG: NLUParser: system_prompt =', system_prompt)
        print('|qm|')#, end='')
        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            # temperature=0.1,
            response_format={
                "type": "json_object"
            },
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": utterance
                }
            ]
        )
        print('|pr|')#, end='')

        content = (
            response
            .choices[0]
            .message
            .content
        )

        data = json.loads(content)

        # print('DEBUG: NLUParser: data =', data)

        parsed = ParsedUtterance(**data)

        print('|val|')#, end='')
        parsed = (
            NLUValidator
            .validate_allowed_values(
                parsed=parsed,
                allowed_languages=self.languages,
                allowed_periods=self.periods,
                allowed_types=self.types,
                allowed_authors=candidates.get("authors"),
                allowed_books=candidates.get("books"),
                allowed_categories=candidates.get("categories"),
                allowed_series=candidates.get("series"),
                allowed_publishers=candidates.get("publishers"),
            )
        )
        parsed = (
            NLUValidator
            .normalize_temporal_constraints(
                parsed
            )
        )
        parsed = (
            NLUValidator
            .normalize_semantic_query(
                parsed
            )
        )
        parsed = (
            NLUValidator
            .preserve_unresolved_mentions(
                parsed=parsed,
                mentions=possible_mentions,
                candidates=candidates,
            )
        )
        parsed = (
            NLUValidator
            .cleanup_unresolved_entities(
                parsed=parsed,
                candidates=candidates,
            )
        )
        print('|pe|')#, end='')

        return parsed
