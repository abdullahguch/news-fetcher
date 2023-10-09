import requests

def get_news(api_key, country='us', category='general', num_articles=5):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'country': country,
        'category': category,
        'pageSize': num_articles
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        news_data = response.json()
        articles = news_data['articles']

        for idx, article in enumerate(articles, start=1):
            print(f"\n--- Article {idx} ---")
            print(f"Title: {article['title']}")
            print(f"Author: {article['author']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("")

    except requests.RequestException as e:
        print(f"Error fetching news: {e}")

if __name__ == "__main__":
    # Input: News API key
    news_api_key = input("Enter your News API key: ")

    # Specify country, category, and the number of articles (adjust as needed)
    country_code = input("Enter country code (e.g., 'us' for United States): ")
    news_category = input("Enter news category (e.g., 'general', 'technology', 'sports'): ")
    num_articles = int(input("Enter the number of articles to fetch: "))

    # Get the latest news
    get_news(news_api_key, country=country_code, category=news_category, num_articles=num_articles)
