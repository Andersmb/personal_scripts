import requests
from bs4 import BeautifulSoup as BS

url = "https://dinebilder.tv2.no/verfoto/"

with requests.session() as sesh:
    fotopage = sesh.get(url)
    soup = BS(fotopage.content, "html.parser")
    tema = soup.find("div", class_="bodyText editBody").getText()

    print(tema)
