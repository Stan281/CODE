import requests
from bs4 import BeautifulSoup as bs
import csv


website_url = 'http://books.toscrape.com/catalogue/dark-notes_800/index.html'
response = requests.get(website_url)
page = response.content
soup = bs(page, features='html.parser')


title = soup.find(class_='col-sm-6 product_main').h1
print(title.text)

#product_description = soup.find('article', class_='product_page').find(id='product_description').next_sibling
#print(product_description)

product_description = soup.find('head').find('meta', attrs={'name':'description'})
print(product_description.attrs['content'].strip())

universal_product_code = soup.find('table',class_='table table-striped')
listetr = universal_product_code.find_all('tr')
book_info={}
for tr in listetr:
	key = tr.th.text
	value = tr.td.text
	book_info[key]=value	
	
#print(listetr)
print(book_info)


'''title  = soup.find_all('article', class_="product_page")
for article in title :
	title = article.h1.text
	print(title)'''
'''
product_description = soup.find('h2', id='product_description')
print(product_description)'''


'''titles = soup.findAll('ol', class_="row")
titles_text = []
for title in titles:
	titles_text.append(title.string)
en_tete = ['titre']
with open('data.csv', 'w') as fichier_csv:
	writer = csv.writer(fichier_csv, delimiter=',')
	writer.writerow(en_tete)
	# zip permet d'itérer sur deux listes à la fois
	for titles in zip(titles_text):
		writer.writerow([titles])'''




