import json

from openai import OpenAI

from RAG.config.settings import settings

from RAG.nlu.entity_extraction.mention_prompts import (
    MENTION_PROMPT
)

from RAG.nlu.entity_extraction.mention_schemas import (
    MentionExtraction
)


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


class MentionExtractor:

    def extract(
        self,
        utterance: str
    ) -> MentionExtraction:

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            # temperature=0,
            response_format={
                "type": "json_object"
            },
            messages=[
                {
                    "role": "system",
                    "content": MENTION_PROMPT
                },
                {
                    "role": "user",
                    "content": utterance
                }
            ]
        )

        data = json.loads(
            response.choices[0]
            .message.content
        )

        # print('DEBUG: MentionExtractor: ', data)

        return MentionExtraction(**data)
