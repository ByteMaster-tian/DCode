from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Static

class InputBox(Vertical):
    """Prompt input area of DCode_project"""
    def compose(self):
        yield Input(
            placeholder="Ask anything, build something....",
            id="prompt"
        )
        yield Static(
            "+ Add context",
            id="prompt-hint"
        )