import requests
from api_key import news_api_key, stock_api_key

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = abs(float(yesterdays_closing_price) - float(day_before_yesterday_closing_price))

diff_percentage = (difference / float(yesterdays_closing_price)) * 100
 
if diff_percentage > 5:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    
    # three articles
    three_articles = articles[:3]
    
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]