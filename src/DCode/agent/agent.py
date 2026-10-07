
from DCode.model.base import ModelProvider

class Agent:
    """Core agent logic."""
    def __init__(self, model: ModelProvider):
        self.model = model

    def run(self, user_input: str) -> str:
        messages = [
            {
                "role": "user",
                "content": user_input
            }
        ]
        return self.model.generate(messages)

    def stream(self, user_input: str):
        messages = [
            {
                "role": "user",
                "content": user_input
            }
        ]
        yield from self.model.stream(messages)