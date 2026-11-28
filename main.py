from dotenv import load_dotenv
from finnhub_client import FinnhubClient
from gemini_model import GeminiModel
from news_summarizer import NewsSummarizer
from telegram_notifier import TelegramNotifier

load_dotenv()

finnhub = FinnhubClient()
summarizer = NewsSummarizer(GeminiModel())
notifier = TelegramNotifier()

quote = finnhub.get_quote("NVDA")
news = finnhub.get_company_news("NVDA", "2026-11-22", "2026-11-23")
summary = (summarizer.summarize("NVDA", quote, news[:10]))
#print(summary)

if summary:
    notifier.send_message(f"NVDA info\n\n{summary}")



