from pathlib import Path

from pydantic import BaseModel

from RAG.config.settings import settings
from RAG.dm.clarification_service import ClarificationService
from RAG.dm.dialog_manager import DialogManager
from RAG.dm.ranking_service import RankingService
from RAG.dm.repositories.books_repository import BooksRepository
from RAG.dm.repositories.chroma_repository import ChromaRepository
from RAG.dm.repositories.state_repository import StateRepository
from RAG.dm.repositories.users_repository import UsersRepository
from RAG.dm.retrieval_service import RetrievalService
from RAG.dm.interaction_service import InteractionService
from RAG.dm.user_profile_service import UserProfileService
from RAG.dm.schemas import DialogResponse
from RAG.nlg.llm_client import LLMClient
from RAG.nlg.nlg_service import NLGService
from RAG.nlg.repositories.prompt_repository import PromptRepository
from RAG.nlg.schemas import BookForNLG
from RAG.nlu.parser import NLUParser
from RAG.nlu.schemas import ParsedUtterance


class RecommenderTurn(BaseModel):
    text: str
    parsed: ParsedUtterance
    dialog_response: DialogResponse


class RecommenderService:
    def __init__(
        self,
        nlu_parser: NLUParser,
        dialog_manager: DialogManager,
        nlg_service: NLGService,
        books_repository: BooksRepository,
        state_repository: StateRepository,
        interaction_service: InteractionService,
    ):
        self.nlu_parser = nlu_parser
        self.dialog_manager = dialog_manager
        self.nlg_service = nlg_service
        self.books_repository = books_repository
        self.state_repository = state_repository
        self.interaction_service = interaction_service

    def handle(
        self,
        user_id: int,
        utterance: str
    ) -> RecommenderTurn:
        parsed = self.nlu_parser.parse(
            utterance,
            dialog_context=self._build_nlu_context(
                user_id
            )
        )
        parsed_for_debug = parsed.model_copy(
            deep=True
        )

        dialog_response = (
            self.dialog_manager.handle(
                user_id,
                parsed
            )
        )

        text = self._generate_text(
            dialog_response,
            utterance
        )

        return RecommenderTurn(
            text=text,
            parsed=parsed_for_debug,
            dialog_response=dialog_response,
        )

    def select_books(
        self,
        user_id: int,
        book_ids: list[str],
    ):
        state = self.state_repository.get(
            user_id
        )
        state.last_selected_books = book_ids
        state.last_selected_book = (
            book_ids[0]
            if book_ids
            else None
        )
        self.state_repository.save(
            state
        )

        for book_id in book_ids:
            self.interaction_service.add_interaction(
                user_id,
                book_id,
                "select",
            )

    def _generate_text(
        self,
        dialog_response: DialogResponse,
        user_utterance: str | None = None,
    ) -> str:
        recommendation_books = []

        if dialog_response.action == "recommend":
            books = (
                self.books_repository
                .get_books_for_nlg(
                    dialog_response.recommendation_ids
                )
            )
            recommendation_books = [
                BookForNLG(**book)
                for book in books
            ]

        return (
            self.nlg_service
            .generate(
                dialog_response,
                user_utterance=user_utterance,
                recommendation_books=recommendation_books,
            )
            .text
        )

    def _build_nlu_context(
        self,
        user_id: int
    ) -> dict:
        state = self.state_repository.get(
            user_id
        )
        focus_books = self.books_repository.get_books(
            state.current_focus_book_ids
        )
        recommended_books = self.books_repository.get_books(
            state.last_recommended_books[:5]
        )
        liked_books = self.books_repository.get_books(
            state.last_liked_book_ids
        )

        return {
            "current_focus_book_ids": (
                state.current_focus_book_ids
            ),
            "current_focus_books": [
                book["name"]
                for book in focus_books
            ],
            "current_focus_authors": (
                state.current_focus_author_names
            ),
            "last_recommended_book_ids": (
                state.last_recommended_books[:5]
            ),
            "last_recommended_books": [
                book["name"]
                for book in recommended_books
            ],
            "last_liked_book_ids": (
                state.last_liked_book_ids
            ),
            "last_liked_books": [
                book["name"]
                for book in liked_books
            ],
            "pending_action": (
                state.pending_action
            ),
            "pending_slots": (
                state.pending_slots
            ),
            "pending_candidates": (
                state.pending_candidates
            ),
        }


def create_default_recommender() -> RecommenderService:
    books_repository = BooksRepository(
        settings.BOOKS_DB_PATH
    )
    users_repository = UsersRepository(
        settings.BOOKS_DB_PATH
    )
    chroma_repository = ChromaRepository(
        settings.CHROMA_DB_PATH
    )
    ranking_service = RankingService()
    clarification_service = ClarificationService()
    retrieval_service = RetrievalService(
        books_repository=books_repository,
        chroma_repository=chroma_repository,
        ranking_service=ranking_service,
        clarification_service=clarification_service,
    )
    profile_service = UserProfileService(
        users_repository=users_repository,
        chroma_repository=chroma_repository,
    )
    interaction_service = InteractionService(
        users_repository=users_repository,
        profile_service=profile_service,
    )
    state_repository = StateRepository()
    dialog_manager = DialogManager(
        retrieval_service=retrieval_service,
        interaction_service=interaction_service,
        state_repository=state_repository,
    )

    prompts_dir = (
        Path(__file__).parent
        /
        "nlg"
        /
        "prompts"
    )
    nlg_service = NLGService(
        llm_client=LLMClient(
            api_key=settings.OPENAI_API_KEY,
            model=settings.OPENAI_MODEL,
        ),
        prompt_repository=PromptRepository(
            str(prompts_dir)
        ),
    )

    return RecommenderService(
        nlu_parser=NLUParser(),
        dialog_manager=dialog_manager,
        nlg_service=nlg_service,
        books_repository=books_repository,
        state_repository=state_repository,
        interaction_service=interaction_service,
    )
