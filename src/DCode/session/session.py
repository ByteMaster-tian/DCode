from uuid import uuid4

class Session:
    """管理单个会话的历史消息"""
    def __init__(self):
        # 每个会话生成唯一ID
        self.session_id = uuid4().hex

        # 保存对话历史
        self.messages = []

    def add_message(self, role: str, content: str):
        """添加一条历史消息"""
        if role not in ("user", "assistant", "system"):
            raise ValueError(f"不支持的消息角色：{role}")
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_messages(self):
        """获取当前会话的历史消息"""
        return [message.copy() for message in self.messages]

    def clear(self):
        """清空当前会话历史"""
        self.message.clear()