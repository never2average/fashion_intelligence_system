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
pagesURL = []
links = []


options = Options() 
options.headless = False
driver = webdriver.Chrome(options=options)

url = 'https://www.myntra.com/' + searchText
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
results = soup.find(id='mountRoot')

while(True): 
    time.sleep(5)
    for product_base in driver.find_elements_by_class_name('product-base'):
        links.append( product_base.find_element_by_xpath('./a').get_attribute("href")) 
        try:
            driver.find_element_by_class_name('pagination-next').click()
        except:
            driver.close()
            driver.quit()

print(links)



