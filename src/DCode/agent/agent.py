import json

from DCode.model.base import ModelProvider
from DCode.session.session import Session
from DCode.roles import MessageRole

SYSTEM_PROMPT = """
你是 DCode，一个智能、多功能的 AI 助手。

你的目标是理解用户的需求，并利用自身知识和能力，
帮助用户高效地解决各种问题。

你可以处理的任务包括但不限于：
1. 知识问答：回答技术、科学、生活等各个领域的问题。
2. 编程开发：代码编写、代码分析、Bug 排查、项目开发和技术方案设计。
3. 内容创作：文章撰写、文本润色、总结归纳和文案创作。
4. 信息分析：逻辑推理、数据分析、问题拆解和方案比较。
5. 学习辅导：解释技术概念、分析原理、提供学习建议。
6. 日常辅助：翻译、信息整理、计划制定等。

回答要求：
1. 优先使用中文回答，根据用户使用的语言灵活调整。
2. 准确理解用户意图，针对问题提供有针对性的回答。
3. 回答尽可能清晰、有条理，避免无意义的内容扩展。
4. 遇到复杂问题时，循序渐进地分析和解释。
5. 对于不确定的信息，应明确说明，不要编造事实。
6. 涉及代码时，尽量提供规范、可读、可运行的代码。
7. 如果用户的需求不明确，可以主动询问必要的信息。
8. 不要声称执行了实际上没有执行的操作。

请始终以专业、友好、高效的方式帮助用户。
"""


class Agent:
    """Core agent logic."""
    def _build_messages(self):
        """构建发送给模型的完整消息"""
        messages = [{
            "role": MessageRole.SYSTEM,
            "content": SYSTEM_PROMPT
        }]
        messages.extend(self.session.get_messages())

        return messages

    def __init__(self, model: ModelProvider, session: Session):
        self.model = model
        self.session = session

    def run(self, user_input: str) -> str:
        """普通输出"""
        # 1.保存当前用户输入
        self.session.add_message(MessageRole.USER, user_input)

        # 2.获取完整对话
        messages = self._build_messages()

        # 3.请求模型
        response = self.model.generate(messages)

        # 4.保存模型回答
        self.session.add_message(MessageRole.ASSISTANT, response)

        return response

    def stream(self, user_input: str):
        """流式输出"""
        # 1.保存当前用户输入
        self.session.add_message(MessageRole.USER, user_input)

        # 2.获取完整对话历史
        messages = self._build_messages()

        # 打印session保存日志
        with open("/Users/darker/Python_project/DCode_project/tests/messages.jsonl", "w", encoding="utf-8") as f:
            for message in messages:
                record = {
                    "session_id": self.session.session_id,
                    **message
                }
                f.write(json.dumps(record,ensure_ascii=False)+"\n")

        # 接收模型流式输出
        response = ""
        for chunk in self.model.stream(messages):
            response += chunk
            yield chunk

        # 4.模型生成结束后保存最终输出
        self.session.add_message(MessageRole.ASSISTANT, response)