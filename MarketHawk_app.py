import requests
from transformers import pipeline
from datetime import datetime

# --- 1. News Fetching Layer ---
def fetch_financial_news():
    # Example: Using NewsAPI (replace with your API key)
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "oil OR dollar OR Trump OR OPEC OR inflation",
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": "3948a40993e44063a210897a0a88e479"
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    return [a["title"] + " - " + a["description"] for a in articles[:10]]

# --- 2. NLP Sentiment Layer ---
def analyze_sentiment(texts):
    sentiment_model = pipeline("sentiment-analysis", model="ProsusAI/finbert")
    results = sentiment_model(texts)
    return results

# --- 3. Insight Aggregator ---
def generate_insight(news, sentiments):
    # Simple aggregation: count bullish vs bearish
    bullish = sum(1 for s in sentiments if s["label"] == "positive")
    bearish = sum(1 for s in sentiments if s["label"] == "negative")
    
    if bullish > bearish:
        insight = "Market sentiment leans bullish today."
    elif bearish > bullish:
        insight = "Market sentiment leans bearish today."
    else:
        insight = "Market sentiment is mixed — caution advised."
    
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "insight": insight,
        "sample_headline": news[0] if news else "No headlines fetched."
    }

# --- 4. Main Bot Runner ---
def run_bot():
    news = fetch_financial_news()
    if not news:
        print("⚠️ No news articles fetched. Check your API key or query.")
        return
    
    sentiments = analyze_sentiment(news)
    insight = generate_insight(news, sentiments)
    print("📊 Market Wizard Insight")
    print(f"Time: {insight['timestamp']}")
    print(f"Insight: {insight['insight']}")
    print(f"Example Headline: {insight['sample_headline']}")


if __name__ == "__main__":
    run_bot()
