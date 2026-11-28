import os
import requests

class TelegramNotifier:
    BASE_URL = "https://api.telegram.org"
    MAX_LEN = 4096

    def __init__(self, token: str | None = None, chat_id: str | None = None):
        self.token = token or os.getenv("TELEGRAM_API_KEY")
        self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
        if not self.token or not self.chat_id:
            raise ValueError("TELEGRAM_API_KEY or TELEGRAM_CHAT_ID missing")


    def send_message(self, text):
        for chunk in self._split(text):
            r = requests.post(
                f"{self.BASE_URL}/bot{self.token}/sendMessage",
                json={"chat_id": self.chat_id, "text": chunk},
                timeout=10
            )
            if not r.ok:
                RuntimeError(f"Telegram error{r.status_code}: {r.text}")

    @classmethod
    def _split(cls, text):
            return [text[i:i + cls.MAX_LEN] for i in range(0, len(text), cls.MAX_LEN)]
