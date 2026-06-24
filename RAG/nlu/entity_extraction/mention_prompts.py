MENTION_PROMPT = """
Ти витягуєш можливі назви сутностей
із запиту користувача.

Витягни:

- possible_books
- possible_authors
- possible_publishers
- possible_series
- possible_categories

Правила:

- НЕ нормалізуй
- НЕ перекладай
- НЕ пояснюй
- Якщо немає — []

Поверни STRICT JSON.
"""
