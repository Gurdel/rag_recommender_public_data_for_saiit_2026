import numpy as np

from RAG.dm.repositories.users_repository import (
    UsersRepository
)

from RAG.dm.repositories.chroma_repository import (
    ChromaRepository
)


class UserProfileService:

    def __init__(
        self,
        users_repository: UsersRepository,
        chroma_repository: ChromaRepository
    ):

        self.users_repository = (
            users_repository
        )

        self.chroma_repository = (
            chroma_repository
        )

    def rebuild_profile(
        self,
        user_id: int
    ):

        ratings = (
            self.users_repository
            .get_user_ratings(
                user_id
            )
        )

        if not ratings:
            return None

        book_ids = [
            r["book_id"]
            for r in ratings
        ]

        embeddings = (
            self.chroma_repository
            .get_book_embeddings(
                book_ids
            )
        )

        profile_vector = None

        for rating_info in ratings:

            book_id = (
                rating_info["book_id"]
            )

            rating = (
                rating_info["rating"]
            )

            embedding = (
                embeddings.get(
                    book_id
                )
            )

            if embedding is None:
                continue

            embedding = (
                np.array(
                    embedding
                )
            )

            weighted_embedding = (
                embedding * rating
            )

            if profile_vector is None:

                profile_vector = (
                    weighted_embedding
                )

            else:

                profile_vector += (
                    weighted_embedding
                )

        if profile_vector is None:
            return None

        profile_vector = (
            profile_vector.tolist()
        )

        self.chroma_repository.upsert_user_embedding(
            user_id=user_id,
            embedding=profile_vector
        )

        return profile_vector
