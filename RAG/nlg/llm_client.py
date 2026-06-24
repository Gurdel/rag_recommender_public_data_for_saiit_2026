from openai import OpenAI


class LLMClient:

    def __init__(
        self,
        api_key: str,
        model: str
    ):

        self.client = OpenAI(
            api_key=api_key
        )

        self.model = model

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:

        response = (
            self.client.chat.completions.create(
                model=self.model,
                # temperature=0.3,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message.content
        )
