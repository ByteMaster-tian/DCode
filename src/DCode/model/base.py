from abc import ABC, abstractmethod

class ModelProvider(ABC):
    """Base interface for model providers."""
    @abstractmethod
    def generate(self, messages: list[dict])->str:
        """Generate a response from the model."""
        raise NotImplementedError

    @abstractmethod
    def stream(self, messages: list[dict]):
        """Generate a streaming response."""
        raise NotImplementedError