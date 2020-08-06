from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import tweepy
import time
import requests
import base64
import os
import html

page = 1
searchText = 't-shirt'
productsURL = []
productName = []
productRating = []
productNoRating = []
productNoRatings = []
productNoReviews = []
pagesURL = []

while page<=1:
    options = Options() 
    options.headless = True
    driver = webdriver.Chrome(options=options)
    
    url = 'https://www.flipkart.com/search?q=' + searchText + '&page=' + str(page)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find(id='container')

    for column in results.findAll(class_='_3dqZjq'):
        column = str(column)
        startIndex = column.find('href="')
        endIndex = column.find('" rel',startIndex)
        pageURL = 'www.flipkart.com' + str((column[startIndex+6:endIndex]).strip())
        pagesURL.append(pageURL)

    for column in results.findAll(class_='_3ZJShS _31bMyl'):
        column = str(column)
        startIndex = column.find('src="')
        endIndex = column.find('"/>',startIndex)
        imageURL = (column[startIndex+5:endIndex]).strip()
        productsURL.append(imageURL)

    i=1
    for a in results.findAll(class_='_2mylT6'):
        driver.switch_to.window(driver.window_handles[0])
        button = driver.find_element_by_link_text(a.text)
        button.click()

        driver.switch_to.window(driver.window_handles[i])

        soup2 = BeautifulSoup(driver.page_source, 'lxml')
        x = soup2.find("div", {"class": "hGSR34 bqXGTW"})

        if x:
            rating = x.text
            print(rating)
            productRating.append(float(rating))
            for y in soup2.find("span", {"class": "_38sUEc"}):
                productNoRating.append(y.text) 
        else:
            productNoRating.append('NA')
            productRating.append(0)
        
        print(a.text)
        productName.append(a.text)

        i+=1

    page = page+1
    driver.quit()

productRatingMean = round(sum(productRating)/len(productRating),2)
productRating = [x if x != 0 else productRatingMean for x in productRating]
for i in productNoRating:
    if i != 'NA':
        j = i.split()
        productNoRatings.append(int(j[0].replace(',', '')))
        productNoReviews.append(int(j[3].replace(',', '')))
    else:
        productNoRatings.append(0)
        productNoReviews.append(0)

tagList = ["" for i in range(len(productName))]

df = pd.DataFrame(
    {
        'product_name': productName,
        'rating': productRating,
        'total_ratings': productNoRatings,
        'total_reviews': productNoReviews, 
        'image_URL': productsURL,
        'page_URL': pagesURL,
        'description': productName,
        'tag_list': tagList
    }
) 
df["item_source"] = "Ecom"
result = df.to_json(orient="records")
fobj = open("results.json", "w")
json.dump(fobj, result)

# df.to_csv('flipkart_scrap.csv', index=False, encoding='utf-8')



