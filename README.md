# Fashion Intelligence System Backend

[![Python](https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6--dev-blue.svg)]()

This is the backend repository for the fashion intelligence system of flipkart grid challenge which was built using the flask backend framework for python and MongoDB document-based database. 


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


