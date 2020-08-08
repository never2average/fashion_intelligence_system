import mongoengine
from models import Product
import json

mongoengine.connect("FIS")

f = open("demosearch_results.json")
j = json.load(f)

for k in j:
    Product(**k).save() 