import json
import random

fake_ml = {
    "tags": ["trendy", "summer", "winter", "leather", "men", "women"],
    "filter": [
        {
            "category_name": 'brand',
            "values": ["roadster", "puma", "wrogn", "ucb", "tommy hilfiger", "jack & jones", "wrangler", "lee", "adidas", "nike"]
        },
        {
            "category_name": "price",
            "values": ["Rs. 179 to Rs. 4882", "Rs. 4882 to Rs. 9585", "Rs. 9585 to Rs. 14288"]
        },
        {
            "category_name": "color",
            "values": ["black", "navy blue", "blue", "white", "grey", "red", "green", "yellow", "maroon", "pink", "mustard"]
        },
        {
            "category_name": "ratings",
            "values": ["4 & above", "3 & above", "2 & above", "1 & above"]
        },
        {
            "category_name": "size",
            "values": ["XXL", "XL", "L", "M", "3XL", "S"]
        },
        {
            "category_name": "occasion",
            "values": ["sports", "casual", "formal", "party", "party", "beach wear", "lounge wear"]
        },
        {
            "category_name": "neck type",
            "values": ["polo", "round", "collared", "V", "hooded", "peter pan"]
        },
        {
            "category_name": "sleeve type",
            "values": ["full", "half", "sleeveless", "short", "puff", "layered", "3/4", "raglan", "roll-up"]
        },
        {
            "category_name": "fabric",
            "values": ["cotton modal lycra blend", "cotton nylon blend", "cotton and polyster mix", "fleece", "polyster lurex blend"]
        },
    ]
}
t = json.load(open("results.json"))
t = json.loads(t)
l = []
l.extend(fake_ml["tags"])
for x in fake_ml["filter"]:
    l.extend(x["values"])
for i in t:
    i["tag_list"] = []
    r = random.randint(3, 15)
    for j in range(r):
        i["tag_list"].append(l[random.randint(0, len(l)-1)])

json.dump(t, open("demosearch_results.json", "w+"))