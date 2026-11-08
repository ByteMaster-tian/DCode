from openai import OpenAI
from DCode.model.base import ModelProvider

class DeepSeekProvider(ModelProvider):
    def __init__(
            self,
            api_key: str,
            model: str = "deepseek-flash",
    ):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        self.model = model

    def generate(self, messages: list[dict]) -> str:
        """阻塞式输出"""
        response = self.client.chat.completions.create(
            model = self.model,
            messages=messages,
            stream=False,
        )
        return response.choices[0].message.content

    def stream(self, messages: list[dict]):
        """流式输出"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
        )
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta.content:
                yield delta.content
