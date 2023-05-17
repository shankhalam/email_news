import requests

api_key = "3bc3669be1304f0a80375d5776034dc4"
url = "https://newsapi.org/v2/top-headlines?country=us&" \
      "category=business&apiKey=" \
      "3bc3669be1304f0a80375d5776034dc4"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
      print(article["title"])
      print(article["content"])