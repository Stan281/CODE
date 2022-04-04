import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'
reponse = requests.get(url)
print(reponse)