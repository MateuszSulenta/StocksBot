class NewsSummarizer:
    PROMPT_TEMPLATE = """Jesteś asystentem streszczającym newsy giełdowe.
Na podstawie WYŁĄCZNIE poniższych wiadomości o spółce {ticker} przygotuj:
- krótkie podsumowanie (max 3 zdania),
- 3 najważniejsze punkty,
- ewentualne ryzyka wspomniane w tekstach.
Nie dodawaj informacji spoza podanych wiadomości. Odpowiadaj po polsku.

{news_text}
"""
    def __init__(self, model):
        self.model = model

    @staticmethod
    def format_news(news: list[dict]) -> str:
        return "\n".join(
            f"- [{n.get('source', '?')}] {n.get('headline', '')}: {n.get('summary', '')}"
            for n in news
        )

    def build_prompt(self, ticker: str, news: list[dict]) -> str:
        return self.PROMPT_TEMPLATE.format(
            ticker = ticker,
            news_text = self.format_news(news)
        )

    def summarize(self, ticker: str, news: list[dict]) -> str | None:
        if not news:
            return None
        response = self.model.invoke(self.build_prompt(ticker, news))
        return self._extract_text(response.content)

    @staticmethod
    def _extract_text(content) -> str:
        if isinstance(content, str):
            return content

        extracted_text = []

        for block in content:
            if isinstance(block, dict):
                text = block.get("text", "")
                extracted_text.append(text)
        return "".join(extracted_text)




