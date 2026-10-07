from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Static, Input
from DCode.ui.chat_view import ChatView
from DCode.ui.input_box import InputBox
from DCode.model import create_model_provider
from DCode.agent.agent import Agent
from DCode.config import config as config
from textual import work

from DCode.ui.message import Message


class DCode(App):
    """DCode_project CLI application"""
    TITLE = "DCode_project"
    SUB_TITLE = "AI Coding Assistant"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        model = create_model_provider(
            config.MODEL_PROVIDER
        )
        self.agent = Agent(model=model)

    CSS = """
    Screen {
        background: #17191e;
    }

    #main {
        width: 100%;
        height: 1fr;
        layout: vertical;
    }

    #welcome {
        width: 100%;
        height: auto;
        align: center middle;
        margin-bottom: 2;
    }

    #logo {
        width: 100%;
        height: auto;
        content-align: center middle;
        color: #8c8f99;
        margin-bottom: 1;
    }

    #welcome-title {
        width: 100%;
        content-align: center middle;
        text-style: bold;
        color: #f0f0f2;
    }

    #welcome-subtitle {
        width: 100%;
        content-align: center middle;
        color: #a7a9b2;
        margin-top: 1;
    }

    #prompt-container {
        width: 100%;
        height: auto;
        border: round #5c5e68;
        padding: 0 1;
        margin-top: 2;
        margin-bottom: 0;
    }
    #prompt-container:focus-within {
        border: round #ff8c00;
    }

    #prompt {
        width: 100%;
        border: none;
        background: transparent;
    }

    #prompt-hint {
        color: #a3a5ae;
        height: 1;
        margin-top: 1;
    }

    #shortcuts {
        width: 100%;
        height: 2;
        align: center middle;
    }

    .shortcut {
        width: 1fr;
        content-align: center middle;
        color: #a3a5ae;
    }
    
    #chat-view {
        width: 100%;
        height: 1fr;
    }
    .message {
        width: 100%;
        height: auto;
        margin: 1 0;
    }
    
    .message-role {
        width: 100%;
        height: 1;
        color: #8c8f99;
        text-style: bold;
    }
    .user-message {
        border-left: solid #3b82f6;
        padding-left: 2;
        margin: 1 0;
    }
    .user-message .message-role {
        color: #60a5fa;
    }
    
    .user-message .message-content {
        color: #e5e7eb;
    }
    
    .message-content {
        width: 100%;
        height: auto;
        color: #e5e7eb;
        padding-left: 2;
    }
    #message-list {
        width: 100%;
        height: auto;
        padding: 1 2;
    }"""

    def on_mount(self):
        self.query_one("#prompt").focus()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main"):
            yield ChatView(id="chat-view")

            yield InputBox(id="prompt-container")

            yield Horizontal(
                Static("Tab: Switch agent", classes="shortcut"),
                Static("/: Commands", classes="shortcut"),
                Static("?: Help", classes="shortcut"),
                id="shortcuts"
            )

    @work(thread = True)
    def run_agent(self, content: str, assistant_message: Message):
        response = ""
        for chunk in self.agent.stream(content):
            response += chunk
            self.call_from_thread(
                self.update_assistant_message,
                assistant_message,
                response
            )

    def update_assistant_message(self, message: Message, content: str):
        message.set_content(content)
        chat_view = self.query_one("#chat-view")
        chat_view.scroll_end(animate=True)

    def on_input_submitted(self, event: Input.Submitted):
        content = event.value.strip()

        if not content:
            return

        chat_view = self.query_one("#chat-view")
        # 添加User Message
        chat_view.add_message(
            role="User",
            content=content
        )

        assistant_message = chat_view.add_assistant_message("")

        self.run_agent(content, assistant_message)

        event.input.value=""
