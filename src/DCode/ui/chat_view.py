from textual.containers import VerticalScroll, Vertical
from textual.widgets import Static

from DCode.ui.message import Message

class ChatView(VerticalScroll):
    """Conversation area of DCode_project"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.has_message = False

    def compose(self):
        with Vertical(id="welcome"):
            yield Static("◆ DCode", id="logo")
            yield Static(
                "Welcome to DCode",
                id="welcome-title"
            )
            yield Static(
                "Your AI coding assistant",
                id="welcome-subtitle"
            )

        # Message 列表
        yield Vertical(id="message-list")

    def on_mount(self):
        self.update_view()

    def update_view(self):
        welcome = self.query_one("#welcome")
        message_list = self.query_one("#message-list")
        if self.has_message:
            welcome.display = False
            message_list.display = True
        else:
            welcome.display = True
            message_list.display = False

    def add_message(self, role: str, content: str):
        """Add a message to the conversation."""
        message_list = self.query_one("#message-list")
        message_list.mount(
            Message(
                role=role,
                content=content
            )
        )

        self.has_message = True
        self.update_view()

        # 自动滚动到底部
        self.scroll_end(animate=False)

    def add_assistant_message(self, content:str):
        """Add a assistant message."""
        message_list = self.query_one("#message-list")
        message = Message(
            role="DCode",
            content=content
        )
        message_list.mount(message)
        self.has_message = True
        self.update_view()
        self.scroll_end(animate=False)

        return message