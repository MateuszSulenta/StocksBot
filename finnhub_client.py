import os
import requests
from datetime import date, timedelta

class FinnhubClient:
    BASE_URL = "https://finnhub.io/api/v1"
    today = date.today()

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("FINNHUB_API_KEY")
        if not self.api_key:
            raise ValueError("FINHUB_API_KEY missing in .env")



    def get_company_news(self, ticker: str, date_from: str, date_to: str) -> list[dict]:
        params = {"symbol": ticker, "from": date_from, "to": date_to, "token": self.api_key}
        r = requests.get(f"{self.BASE_URL}/company-news", params=params, timeout=10)
        r.raise_for_status()
        return r.json()
