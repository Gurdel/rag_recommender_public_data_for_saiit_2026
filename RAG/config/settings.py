import os
from pathlib import Path

from dotenv import load_dotenv

RAG_ENV_PATH = Path(__file__).resolve().parents[1] / ".env"

load_dotenv(RAG_ENV_PATH)
load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    BOOKS_DB_PATH = os.getenv("BOOKS_DB_PATH")
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-5-mini"
    )

    DEFAULT_USER_ID = int(
        os.getenv(
            "DEFAULT_USER_ID",
            "1"
        )
    )


settings = Settings()
