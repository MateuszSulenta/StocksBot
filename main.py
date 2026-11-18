import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import requests
import yfinance as yf
from datetime import date, timedelta

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY
                        )

today = date.today()
params = {
    "symbol": "NVDA",
    "from": (today - timedelta(days=7)).isoformat(),
    "to": today.isoformat(),
    "token": FINNHUB_API_KEY,
}
r = requests.get("https://finnhub.io/api/v1/company-news", params=params, timeout=10)
r.raise_for_status()
for item in r.json()[:5]:
    print(item["headline"], item["summary"], item["url"])





#response = model.invoke("Bitcoin will be increase in next couple of months?")
#print(response.content[0]['text'])

tsla = yf.Ticker("TSLA")
news = tsla.news

msft = yf.Ticker("MSFT")



# for item in news:
#     content = item.get("content", {})
#     print(content.get("title"))
#     print(content.get("pubDate"))
#     print(content.get("summary"))
#     print(content.get("canonicalUrl", {}).get("url"))
#     print("-" * 40)



