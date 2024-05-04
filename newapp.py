import requests
import json
query = input("Enter the topics: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-04-03&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"
r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("################################")

