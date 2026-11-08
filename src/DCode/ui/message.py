from textual.containers import Vertical
from textual.widgets import Static
from rich.markdown import Markdown
from DCode.roles import MessageRole

class Message(Vertical):
    """A Single conversation message."""
    def __init__(
            self,
            role: str,
            content: str,
            **kwargs
    ):
        if role == MessageRole.USER:
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
            Markdown(self.content),
            classes="message-content"
        )

    def set_content(self, content:str):
        """Update message content.将大模型响应消息渲染到GUI界面上，支持markdown格式渲染"""
        self.content = content
        content_weight = self.query_one(
            ".message-content",
            Static
        )
        content_weight.update(Markdown(content))
