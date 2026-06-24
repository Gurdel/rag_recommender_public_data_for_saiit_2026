class ExplanationService:

    def build_reason(
        self,
        retrieval_type: str,
        reason: str
    ) -> str:

        mapping = {

            "profile":
                "Рекомендації сформовані на основі ваших попередніх оцінок.",

            "semantic":
                "Книги підібрані за змістом вашого запиту.",

            "hybrid":
                "Книги відповідають вашим фільтрам і впорядковані за релевантністю.",

            "author":
                "Книги вибрані за вказаним автором.",

            "similar_book":
                "Книги схожі на ту, яку ви згадали.",

            "too_many_structured_constraints":
                "Знайдено багато книг за вашими критеріями, тому вибрані найбільш релевантні з урахуванням профілю.",

            "too_many_semantic_and_constraints":
                "Знайдено багато книг за фільтрами і змістом запиту, тому вибрані найбільш релевантні."
        }

        return mapping.get(
            retrieval_type,
            reason
        )
