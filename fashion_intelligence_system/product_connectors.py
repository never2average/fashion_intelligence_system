from models import Product
import json
from authorization import validateToken
import math
import re
from collections import Counter


def product_details(product_id, amount):
    if amount == "full":
        return Product.objects.get(id=product_id).to_json(), 200
    else:
        return Product.objects.get(id=product_id).only(
            "img_url","product_url"
        ).to_json(), 200


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    WORD = re.compile(r"\w+")
    words = WORD.findall(text)
    return Counter(words)


def similar_products(search_id, product_id):
    fobj = open("/home/ubuntu/"+str(search_id)+"_results.json")
    data = json.load(fobj)
    data_to_plot = []
    main_i = [i for i in data if i["_id"]["$oid"] == product_id][0]
    main_str = text_to_vector(main_i["product_description"])
    for i in data:
        new = [0,0,0,0]
        try:
            new[0] = i["product_ratings"]*i["product_num_ratings"]
            new[0] = new[0]/i["product_num_reviews"]
        except:
            new[0] = 0
        new[1] = hash(tuple(i["tags_list"]))
        new[2] = get_cosine(
            main_str, 
            text_to_vector(i["product_description"])
        )
        new[3] = i["_id"]["$oid"]
        data_to_plot.append(new)
    return json.dumps(data_to_plot), 200