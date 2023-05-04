import requests
from send_email import send_email
from environs import Env


env = Env()
env.read_env()
topic = "tesla"

api_key = env("NEWSAPI")


url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&apiKey=" \
      "34a11a04845f4dbe98f8422bab14fd9e&" \
      "language=en"

request = requests.get(url)
content = request.json()
subject = "Subject: Today's News"

body = subject + "\n" * 2
# [:20] means send only 20 articles
for article in content["articles"][:20]:
    if article['title'] is not None:
        body += article['title'] \
               + "\n"\
               + article["description"] \
               + "\n" + article['url'] \
               + 2*"\n"

body = body.encode("utf-8")
send_email(body)

