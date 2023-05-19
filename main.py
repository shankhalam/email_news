# Import Libraries
import requests
from send_mail import send_mail

# API key from site
api_key = "3bc3669be1304f0a80375d5776034dc4"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=us&" \
      "category=business&" \
      "apiKey=""3bc3669be1304f0a80375d5776034dc4&" \
      "language=en"

request = requests.get(url)
content = request.json()

# Body of message(email)
body = ""
for article in content["articles"][0:20]:
    if article["description"] is not None:
        body = "Subject: Today's News" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = body.encode('utf-8')
send_mail(message=body)

