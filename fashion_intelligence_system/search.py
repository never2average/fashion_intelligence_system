import json

def search(search_text, result_type):
    return json.dumps({"id": "demosearch"}), 200


def search_metadata(search_id):
    return json.dumps(
        json.load(open(str(search_id)+"_metadata.json"))
    ), 200


def search_results(search_id, pageno):
    fobj = open(str(search_id)+"_results.json")
    return json.dumps(
        json.load(fobj)[(pageno-1)*10:pageno*10]