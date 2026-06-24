from pathlib import Path


class PromptRepository:

    def __init__(
        self,
        prompts_dir: str
    ):
        self.prompts_dir = Path(prompts_dir)

    def load(
        self,
        name: str
    ) -> str:

        path = self.prompts_dir / name

        return path.read_text(
            encoding="utf-8"
        )
