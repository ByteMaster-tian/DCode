import os
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

def print_tree(root_dir: str):
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, "").count(os.sep)
        indent = "  "*level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = "  "*(level+1)
        for file in files:
            print(f"{sub_indent}{file}")

class MiniOpencCode(App):
    """Mini OpenCode CLI Application"""
    TITLE = "Mini OpenCode"
    SUB_TITLE = "AI Coding Assistant"
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Welcome to Mini OpenCode!", id="welcome")
        yield Footer()


if __name__ == "__main__":
    # app = MiniOpencCode()
    # app.run()
    print_tree("/")