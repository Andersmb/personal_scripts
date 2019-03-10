#coding: utf-8
import requests
from bs4 import BeautifulSoup as BS

url = "https://dinebilder.tv2.no/verfoto/"

with requests.session() as sesh:
    fotopage = sesh.get(url)
    soup = BS(fotopage.content, "html.parser")
    tema = soup.find("div", class_="bodyText editBody").get_text()

    special = {u"æ": u"ae",
               u"ø": u"oe",
               u"å": u"aa"}

# replace any Norwegian characters
for char in tema:
    for x, y in special.items():
        if char == x:
            tema = tema.replace(x, y)

print(tema)
