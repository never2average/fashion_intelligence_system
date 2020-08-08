import pymongo
from models import Product
import json

c = pymongo.MongoClient()
coll = c.FIS.product

f = open("demosearch_results.json")
j = json.load(f)

coll.insert_many(j)