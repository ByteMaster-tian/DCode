from DCode.model.base import ModelProvider
from DCode.model.mock import MockModelProvider
from DCode.model.deepseek import DeepSeekProvider
from DCode.config import config as config


def create_model_provider(
        provider: str,
        **kwargs
) -> ModelProvider:
    if provider == "mock":
        return MockModelProvider()
    elif provider == "deepseek":
        if not config.DEEPSEEK_API_KEY:
            raise ValueError("DEEPSEEK_API_KEY is not configured")
        return DeepSeekProvider(
            api_key=config.DEEPSEEK_API_KEY,
            model=config.DEEPSEEK_MODEL
        )

    raise ValueError(f"Unsupported model provider; {provider}")