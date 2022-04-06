import requests
from bs4 import BeautifulSoup as bs
import csv


url = 'http://books.toscrape.com/catalogue/dark-notes_800/index.html'
response = requests.get(url)
page = response.content

soup = bs(page, features='html.parser')

articles = soup.find_all("article", class_="product_page")
for article in articles:
	title = article.h1.text
	print(title)

'''title = soup.findAll('h1', class_="col-sm-6 product_main")
print(title)'''

'''product_description = soup.findAll('article'="description")
print(product_description)'''


"""titles = soup.findAll('ol', class_="row")
titles_text = []
for title in titles:
	titles_text.append(title.string)

en_tete = ['titre']
with open('data.csv', 'w') as fichier_csv:
	writer = csv.writer(fichier_csv, delimiter=',')
	writer.writerow(en_tete)
	# zip permet d'itérer sur deux listes à la fois
	for titles in zip(titles_text):
		writer.writerow([titles])






#descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")"""