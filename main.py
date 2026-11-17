import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import requests
import yfinance as yf

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY
                        )

#response = model.invoke("Bitcoin will be increase in next couple of months?")
#print(response.content[0]['text'])

tsla = yf.Ticker("TSLA")
news = tsla.news

for item in news:
    content = item.get("content", {})
    print(content.get("title"))
    print(content.get("pubDate"))
    print(content.get("summary"))
    print(content.get("canonicalUrl", {}).get("url"))
    print("-" * 40)



