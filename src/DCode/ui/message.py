from textual.containers import Vertical
from textual.widgets import Static

class Message(Vertical):
    """A Single conversation message."""
    def __init__(
            self,
            role: str,
            content: str,
            **kwargs
    ):
        if role == "User":
            kwargs.setdefault("classes", "message user-message")
        else:
            kwargs.setdefault("classes", "message")
        super().__init__(**kwargs)

        self.role = role
        self.content = content

    def compose(self):
        yield Static(
            self.role,
            classes="message-role"
        )
        yield Static(
            self.content,
            classes="message-content"
        )

    def set_content(self, content:str):
        """Update message content."""
        self.content = content
        content_weight = self.query_one(
            ".message-content",
            Static
        )
        content_weight.update(content)
