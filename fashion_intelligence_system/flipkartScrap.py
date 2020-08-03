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
productHref = []
productRating = []

while page<=5:
    options = Options() 
    options.headless = False
    driver = webdriver.Chrome(options=options)
    
    url = 'https://www.flipkart.com/search?q=' + searchText + '&page=' + str(page)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find(id='container')

    # for column in results.findAll(class_='_3ZJShS _31bMyl'):
    #     column = str(column)
    #     startIndex = column.find('src="')
    #     endIndex = column.find('"/>',startIndex)
    #     imageURL = (column[startIndex+5:endIndex]).strip()
    #     print(imageURL)

    for a in results.findAll(class_='_2mylT6'):
        button = driver.find_element_by_link_text(a.text)
        button.click()

        driver.switch_to.window(driver.window_handles[1])

        soup2 = BeautifulSoup(driver.page_source, 'lxml')
        results2 = soup2.find(id='container')

        x = results2.find('hGSR34 bqXGTW')
        #print(results2)
        rating = x.text
        print(rating)
        productRating.append(rating)
        # for y in results2.find_elements_by_xpath('.//span[@class = "_38sUEc"]'):
        #     print(y.text)
        productName.append(a.text)


    page = page+1
    driver.quit()
