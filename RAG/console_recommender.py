#!/usr/bin/env python3

import json

from RAG.config.settings import settings
from RAG.recommender_service import create_default_recommender


HELP_TEXT = """
Commands:
  /help              show this help
  /user <id>         switch user id
  /last              print last recommendation ids
  /select <items>    select books by 1-based indexes from last results or by ids
  /quit              exit

Any other input is sent to the recommender.
"""

GREETING = """
Привіт! Я — рекомендаційний бот українських книг.  
Напиши мені категорії, авторів чи будь‑які інші обмеження, і я підберу для тебе щось цікаве почитати. 
Можу радити класику, сучасну прозу, поезію, наукову літературу чи навіть вузькі теми — усе залежить від твоїх вподобань.
"""


def _pretty(data) -> str:
    return json.dumps(
        data,
        ensure_ascii=False,
        indent=2,
    )


def _resolve_selection(
    items: list[str],
    last_recommendation_ids: list[str],
) -> list[str]:
    selected = []

    for item in items:
        if item.isdigit():
            index = int(item) - 1
            if 0 <= index < len(last_recommendation_ids):
                selected.append(
                    last_recommendation_ids[index]
                )
                continue

        selected.append(
            item
        )

    return selected


def main():
    recommender = create_default_recommender()
    user_id = settings.DEFAULT_USER_ID
    last_recommendation_ids = []

    print("Ukrainian books recommender console")
    print("Type /help for commands, /quit to exit.")
    print(f"Current user_id: {user_id}")

    print(GREETING)

    while True:
        try:
            utterance = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not utterance:
            continue

        if utterance == "/quit":
            break

        if utterance == "/help":
            print(HELP_TEXT.strip())
            continue

        if utterance.startswith("/user "):
            _, raw_user_id = utterance.split(
                maxsplit=1
            )
            try:
                user_id = int(raw_user_id)
            except ValueError:
                print("user_id must be an integer")
                continue

            print(f"Current user_id: {user_id}")
            continue

        if utterance == "/last":
            print(
                _pretty(
                    {
                        "recommendation_ids": (
                            last_recommendation_ids
                        )
                    }
                )
            )
            continue

        if utterance.startswith("/select "):
            items = utterance.split()[1:]
            selected_book_ids = _resolve_selection(
                items,
                last_recommendation_ids,
            )
            recommender.select_books(
                user_id,
                selected_book_ids,
            )
            print(
                _pretty(
                    {
                        "selected_book_ids": (
                            selected_book_ids
                        )
                    }
                )
            )
            continue

        try:
            turn = recommender.handle(
                user_id,
                utterance,
            )
        except Exception as exc:
            print("\n[ERROR]")
            print(f"{type(exc).__name__}: {exc}")
            continue

        last_recommendation_ids = (
            turn
            .dialog_response
            .recommendation_ids
        )

        print("\n[NLU]")
        print(
            _pretty(
                turn.parsed.model_dump()
            )
        )

        print("\n[DM]")
        print(
            _pretty(
                turn.dialog_response.model_dump()
            )
        )

        print("\n[NLG]")
        print(turn.text)


if __name__ == "__main__":
    print(HELP_TEXT)
    main()
