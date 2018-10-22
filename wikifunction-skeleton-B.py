"""
To see an example of the Wikipedia API JSON look at this url:
https://en.wikipedia.org/api/rest_v1/page/summary/Japanese_cuisine
"""
import requests

def wiki_source(title, value):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = requests.get(url)

    if req.status_code != 200:
        print(f"We got an error: {req.status_code}")
        exit()
    else:
        data = req.json()
        if value == "extract":
            return data["extract"]
        elif value == "description":
            return data["description"]

title = input("What are you searching for? ").strip().replace(" ","_")
value = input("Do you want the description or extract ").strip().lower()

data = wiki_source(title, value)

print(data)
