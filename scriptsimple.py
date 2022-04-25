import requests
from bs4 import BeautifulSoup
import re

url = 'http://books.toscrape.com/catalogue/dark-notes_800/index.html'
response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, 'html.parser')

book = soup.find_all("article", class_="product_page") 
for article in book:
    img_url = article.find("img")["src"]
    title = article.h1.text
    product_information = article.find("table", class_="table table-striped")
    product_information_row = product_information.find_all("tr")
    upc_code = product_information_row[0].find("td").text
    price_including_tax = product_information_row[2].find("td").text
    price_excluding_tax = product_information_row[3].find("td").text
    number_available = product_information_row[5].find("td").text
    product_description = article.find("div", class_= "sub-header").findNext("p").text
    #product_description = soup.select('article > p')[0].text
    review_rating = article.find("p", class_= re.compile(r'star-rating'))
    nb_rating = len(review_rating.find_all("i"))
category = soup.find("ul", class_="breadcrumb")
book_category = category.find_all("li")[-2].find("a").text

with open('book.csv', 'w+') as extract:
    extract.write('product_page_url, universal_ product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url \n')
    extract.write(url + ',' + upc_code + ',' + title + ',' + price_including_tax + ',' + price_excluding_tax + ',' + number_available + ',' + product_description + ',' + book_category + ',' +  str(nb_rating) + ',' + img_url + '\n')



