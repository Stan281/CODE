import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd

website_url = 'http://books.toscrape.com/catalogue/dark-notes_800/index.html'
response = requests.get(website_url)
page = response.content
soup = bs(page, features='html.parser')

product_page_url = response.url
print(product_page_url)

universal_product_code = soup.find('table',class_='table table-striped')
listetr = universal_product_code.find_all('tr')
book_info={}
for tr in listetr:
	key = tr.th.text
	value = tr.td.text
	book_info[key]=value

print(book_info)

title = soup.find(class_='col-sm-6 product_main').h1
print(title.text)

product_description = soup.find('head').find('meta', attrs={'name':'description'})
print(product_description.attrs['content'].strip())

img_url = soup.find("img")["src"]
print(img_url)


'''with open('book.csv', 'w+') as extract:
    extract.write('product_page_url, universal_ product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url \n')
    extract.write(website_url + ',' + book_info{} + ',' + title + ',' + product_description + ',' + img_url + '\n')'''

'''with open('data.csv', 'w') as fichier_csv:
	writer = csv.writer(fichier_csv, delimiter=',')
	writer.writerow('product_page_url, universal_ product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url')
	for titles in zip(title):
		writer.writerow([titles])'''

'''with open('book.csv', 'w+') as extract:
    extract.write('product_page_url, universal_ product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url \n')
    extract.write(website_url + ',' + book_info + ',' + title + product_description + img_url + '\n')'''

'''df=pd.DataFrame(book_info,columns=['product_page_url','universal_product_code','product_type','price_excluding_tax','price_including_tax','tax','number_available','title','product_description','image_url'])
df.to_csv('extractbook.csv')'''

'''df=pd.DataFrame(book_info,columns=['product_page_url','universal_product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url'])
df.to_csv('extractbook.csv')'''


'''with open('data.csv', 'w') as fichier_csv:
	writer = csv.writer(fichier_csv, delimiter=',')
	writer.writerow(en_tete)'''
# zip permet d'it??rer sur deux listes ?? la fois
'''for titles in zip(titles_text):
		writer.writerow([titles])'''




