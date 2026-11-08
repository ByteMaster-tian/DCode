import os

MODEL_PROVIDER = os.getenv(
    "DCODE_MODEL_PROVIDER",
    "mock"
)

DEEPSEEK_API_KEY = os.getenv(
    "DEEPSEEK_API_KEY"
)

DEEPSEEK_MODEL = os.getenv(
    "DEEPSEEK_MODEL",
    "deepseek-flash"
)