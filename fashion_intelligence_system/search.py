import json

def search(search_text, result_type):
    return json.dumps({"id": "demosearch"}), 200


def search_metadata(search_id):
    fobj = open(str(search_id)+"_metadata.json")
    return json.dumps(json.load(fobj)), 200


def search_results(search_id, pageno):
    fobj = open(str(search_id)+"_results.json")
    return json.dumps(json.load(fobj)[pageno]), 200