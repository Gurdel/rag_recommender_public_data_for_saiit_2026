from RAG.dm.repositories.users_repository import (
    UsersRepository
)

from RAG.dm.user_profile_service import (
    UserProfileService
)


class InteractionService:

    def __init__(
        self,
        users_repository: UsersRepository,
        profile_service: UserProfileService
    ):

        self.users_repository = (
            users_repository
        )

        self.profile_service = (
            profile_service
        )

    def save_rating(
        self,
        user_id: int,
        book_id: str,
        rating: int
    ):

        self.users_repository.save_rating(
            user_id,
            book_id,
            rating
        )

        self.profile_service.rebuild_profile(
            user_id
        )

    def add_interaction(
        self,
        user_id: int,
        book_id: str,
        interaction_type: str
    ):

        self.users_repository.add_interaction(
            user_id,
            book_id,
            interaction_type
        )