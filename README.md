# Fashion Intelligence System Backend ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

### Documentation Added to GitBook [Link](https://fashion-intelligence-system.gitbook.io/fashion-intelligence-system-backend/)

[![Python](https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6--dev-blue.svg)]()

This is the backend repository for the fashion intelligence system of flipkart grid challenge which was built using the flask backend framework for python and MongoDB document-based database. 


## Hosted API

In order to use the hosted version of the API endpoints created in this project, you can view the documentation of the [postman collection](https://documenter.getpostman.com/view/5663727/T1LJkoh7)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/a2e5616744cec90c4f96)

## Getting started

Installation instructions are only for debian based systems:

```shell
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install python3-venv
git clone https://github.com/never2average/fashion_intelligence_system
cd fashion_intelligence_system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd fashion_intelligence_system
python3 app.py
```

In order to run the following project on a server so that it is accessible over the web, check out the following instructions for [Flask apps with UWSGI and Nginx](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)


## Webscrapping using Selenium

We have used selenium along with beautiful soup for web scraping the fashion data from various sources.
Sources we have scraped for now are:    
* [flipkart](flipkart.com)   
* [myntra](myntra.com)    
* [vogue](vogue.com)   
* [instagram](instagram.com)   

**Why we have used selenium?**    
*Web scraping with Python and Beautiful Soup is an excellent tool to have within your skillset. It's useful only when the data you need to work with is available to the public, but not necessarily conveniently available. When JavaScript provides or “hides” content, browser automation with Selenium will insure your code “sees” what you (as a user) should see. And finally, when you are scraping tables full of data, pandas is the Python data analysis library that will handle it all.*

### Installation

We will use Chrome in our example, so make sure you have it installed on your local machine:

> * [Chrome download page](https://www.google.com/chrome/)    
> * [Chrome driver binary](https://sites.google.com/a/chromium.org/chromedriver/downloads)    
> * selenium package    

In order to install the Selenium package, I recommend that you create a virtual environnement, using virtualenv and then:

```sh
$ pip3 install selenium
```


