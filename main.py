import os
from dotenv import load_dotenv
from finnhub_client import FinnhubClient
from gemini_model import GeminiModel
from news_summarizer import NewsSummarizer

load_dotenv()

finnhub = FinnhubClient()
summarizer = NewsSummarizer(GeminiModel())

news = finnhub.get_company_news("NVDA", "2026-11-22", "2026-11-23")
print(summarizer.summarize("NVDA", news[:10]))
