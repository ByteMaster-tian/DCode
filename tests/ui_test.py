from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Footer, Static, Input

class MiniOpenCode(App):
    """Mini OpenCode CLI application"""
    TITLE = "Mini OpenCode"
    SUB_TITLE = "AI Coding Assistant"
    CSS = """
    Screen {
        background: #17191e;
    }

    #main {
        width: 100%;
        height: 1fr;
        align: center middle;
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
        max-width: 90;
        height: auto;
        border: round #5c5e68;
        padding: 0 1;
        margin-top: 2;
        margin-bottom: 0;
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
    }"""

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main"):
            with Vertical(id="welcome"):
                yield Static("◆ DCode_project", id="logo")
                yield Static(
                    "Welcome to Mini OpenCode",
                    id="welcome-title"
                )
                yield Static(
                    "Your AI coding assistant",
                    id="welcome-subtitle"
                )
            with Vertical(id="prompt-container"):
                yield Input(
                    placeholder="Ask anything, build something....",
                    id="prompt"
                )
                yield Static(
                    "+ Add context",
                    id="prompt-hint"
                )
            yield Horizontal(
                Static("Tab: Switch agent", classes="shortcut"),
                Static("/: Commands", classes="shortcut"),
                Static("?: Help", classes="shortcut"),
                id="shortcuts"
            )

if __name__ == "__main__":
    app = MiniOpenCode()
    app.run()