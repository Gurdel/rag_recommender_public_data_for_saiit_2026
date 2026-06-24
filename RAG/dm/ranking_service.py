import numpy as np


class RankingService:

    @staticmethod
    def cosine_similarity(
        vector_a,
        vector_b
    ):

        vector_a = np.array(vector_a)
        vector_b = np.array(vector_b)

        denominator = (
            np.linalg.norm(vector_a)
            *
            np.linalg.norm(vector_b)
        )

        if denominator == 0:
            return 0.0

        return float(
            np.dot(
                vector_a,
                vector_b
            ) / denominator
        )

    def rank_books(
        self,
        user_embedding,
        book_embeddings
    ):

        scored_books = []

        for (
            book_id,
            embedding
        ) in book_embeddings.items():

            score = (
                self.cosine_similarity(
                    user_embedding,
                    embedding
                )
            )

            scored_books.append(
                (
                    book_id,
                    score
                )
            )

        scored_books.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return scored_books
