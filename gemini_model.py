import os
from langchain.chat_models import init_chat_model

class GeminiModel:
    def __init__(self, model_name: str = "gemini-3-flash-preview", api_key: str | None = None):
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY missing in .env")
        self._model = init_chat_model(
            model=model_name,
            model_provider="google-genai",
            api_key=api_key
        )

    def invoke(self, prompt:str):
        return self._model.invoke(prompt)