import os

from src.DCode.model import DeepSeekProvider

def main():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("请先设置 DEEPSEEK_API_KEY 环境变量")

    model = DeepSeekProvider(api_key= api_key)
    messages = [
        {
            "role": "user",
            "content": "你好，请简单介绍一下你自己。"
        }
    ]

    # response = model.generate(messages)
    print("\n========== DeepSeek Response ==========")
    for chunk in model.stream(messages):
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    main()