import runpy

import requests
from send_mail import send_mail

api_key = "3bc3669be1304f0a80375d5776034dc4"
url = "https://newsapi.org/v2/top-headlines?country=us&" \
      "category=business&apiKey=" \
      "3bc3669be1304f0a80375d5776034dc4"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode('utf-8')
send_mail(message=body)

