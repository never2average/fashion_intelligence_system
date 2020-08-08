import json
from models import Product

def make_ngrams(word, min_size=2, prefix_only=False):
    length = len(word)
    size_range = range(min_size, max(length, min_size) + 1)
    if prefix_only:
        return [
            word[0:size]
            for size in size_range
        ]
    return list(set(
        word[i:i + size]
        for size in size_range
        for i in range(0, max(0, length - size) + 1)
    ))


def search(search_text, result_type):
    search_text = ''.join([x for x in search_text if x==" " or x.isalpha()])
    grams = make_ngrams(search_text)
    p = json.loads(Product.objects(item_source="Ecom").to_json())
    json.dump(p, open("/home/ubuntu/demosearch_metadata.json"))
    return json.dumps({"id": "demosearch", "pages": len(p)}), 200


def search_metadata(search_id):
    return json.dumps(
        json.load(open("/home/ubuntu/"+str(search_id)+"_metadata.json"))
    ), 200


def search_results(search_id, pageno):
    pageno = int(pageno)
    fobj = open(str(search_id)+"_results.json")
    return json.dumps(
        json.load(fobj)[(pageno-1)*10:pageno*10]
    ), 200
