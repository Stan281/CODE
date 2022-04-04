import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'
response = requests.get(url)
page = response.content

soup = BeautifulSoup(page, features='html.parser')

title = soup.find('title')
print(title.text)