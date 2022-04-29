import requests
from bs4 import BeautifulSoup
import csv
import re

def scraping_product(url):

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
        review_rating = article.find("p", class_= re.compile(r'star-rating'))
        nb_rating = len(review_rating.find_all("i"))
        category = soup.find("ul", class_="breadcrumb")
        book_category = category.find_all("li")[-2].find("a").text


    content = url + ';' + upc_code + ';' + title + ';' + price_including_tax + ';' + price_excluding_tax + ';' + number_available + ';' + product_description + ';' + book_category + ';' + str(nb_rating) + ';' + img_url + '\n'
    return content

response = requests.get("https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html")
html = response.content
soup = BeautifulSoup(html, 'html.parser')   

articles = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")  # parent
content = ""
for article in articles:
    h3 = article.find("h3")
    a = h3.find("a")
    href = a["href"]
    title = a["title"]
    href = href.replace("../../../","https://books.toscrape.com/catalogue/" )
    content += scraping_product(href)

with open('category.csv', 'w+') as extract:
    extract.write('product_page_url;universal_product_code(upc);title;price_including_tax;price_excluding_tax;number_available;product_description;category;review_rating;image_url \n')
    extract.write(content)


