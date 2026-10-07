from DCode.model.base import ModelProvider

class MockModelProvider(ModelProvider):
    """Mock model provider for development."""
    def generate(self, messages: list[dict]) ->str:
        last_message = messages[-1]["content"]
        return f"我收到了你的消息：{last_message}"

    def stream(self, messages: list[dict]):
        response = "这是一个 Mock 模型的流式回复"
        for char in response:
            yield char