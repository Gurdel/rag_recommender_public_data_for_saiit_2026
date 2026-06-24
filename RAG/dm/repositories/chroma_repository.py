from typing import Optional

import chromadb


class ChromaRepository:

    def __init__(
        self,
        chroma_path: str
    ):

        self.client = chromadb.PersistentClient(
            path=chroma_path
        )

        self.books_collection = (
            self.client.get_collection(
                "books"
            )
        )

        self.users_collection = (
            self.client.get_or_create_collection(
                "users"
            )
        )

    # -----------------------------
    # BOOK SEARCH
    # -----------------------------

    def semantic_search(
        self,
        query_text: str,
        candidate_book_ids: Optional[list[str]] = None,
        top_k: int = 20
    ):

        if not query_text:
            return []

        if candidate_book_ids:
            results = self.books_collection.query(
                query_texts=[query_text],
                n_results=top_k,
                where={"id": {"$in": candidate_book_ids}},
            )
        else:
            results = self.books_collection.query(
                query_texts=[query_text],
                n_results=top_k,
            )

        ids = results["ids"][0]
        distances = results["distances"][0]

        books = [
            {
                "id": book_id,
                "distance": distance
            }
            for book_id, distance
            in zip(ids, distances)
        ]

        books.sort(
            key=lambda x: x["distance"]
        )

        return books[:top_k]

    # -----------------------------
    # EMBEDDINGS
    # -----------------------------

    def get_book_embeddings(
        self,
        book_ids: list[str]
    ):

        if not book_ids:
            return {}

        result = self.books_collection.get(
            ids=book_ids,
            include=["embeddings"]
        )

        return {
            book_id: embedding
            for book_id, embedding
            in zip(
                result["ids"],
                result["embeddings"]
            )
        }
    

    def query_by_embedding(
        self,
        embedding,
        top_k: int = 20
    ):

        result = (
            self.books_collection.query(
                query_embeddings=[
                    embedding
                ],
                n_results=top_k
            )
        )

        return [
            {
                "id": book_id,
                "distance": distance
            }
            for (
                book_id,
                distance
            )
            in zip(
                result["ids"][0],
                result["distances"][0]
            )
        ]
    

    def recommend_similar_book(
        self,
        book_id: str,
        top_k: int = 20
    ):

        result = self.books_collection.get(
            ids=[book_id],
            include=["embeddings"]
        )

        if not result["ids"]:
            return []

        embedding = (
            result["embeddings"][0]
        )

        neighbours = (
            self.query_by_embedding(
                embedding,
                top_k=top_k + 1
            )
        )

        neighbours = [
            item
            for item in neighbours
            if item["id"] != book_id
        ]

        return neighbours[:top_k]


    # -----------------------------
    # USER PROFILE
    # -----------------------------

    def get_user_embedding(
        self,
        user_id: int
    ):

        result = self.users_collection.get(
            ids=[str(user_id)],
            include=["embeddings"]
        )

        if not result["ids"]:
            embedding = (
                self.create_zero_user_embedding(
                    user_id
                )
            )
            return embedding

        return result["embeddings"][0]

    def create_zero_user_embedding(
        self,
        user_id: int
    ):
        dimension = (
            self._book_embedding_dimension()
        )
        if dimension is None:
            return None

        embedding = [
            0.0
            for _ in range(dimension)
        ]

        self.upsert_user_embedding(
            user_id,
            embedding
        )

        return embedding

    def _book_embedding_dimension(
        self
    ) -> int | None:
        result = self.books_collection.get(
            limit=1,
            include=["embeddings"]
        )

        embeddings = result.get(
            "embeddings",
            []
        )
        if len(embeddings) == 0:
            return None

        return len(
            embeddings[0]
        )

    def upsert_user_embedding(
        self,
        user_id: int,
        embedding: list[float]
    ):

        self.users_collection.upsert(
            ids=[str(user_id)],
            embeddings=[embedding]
        )
