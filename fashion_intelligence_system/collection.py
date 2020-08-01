from models import Collection
import json
from authorization import validateToken


def create_collection(token, collection_name):
    tokenValidator = validateToken(token)
    if not tokenValidator[0]:
        return {"error": "UnauthorizedError"}, 401
    else:
        user = tokenValidator[1]
        c = Collection(collection_name=collection_name)
        c.save()
        user.update(add_to_set__my_collections=[c])
        return {"message": "Collection Created Successfully"}, 200


def list_collection(token):
    tokenValidator = validateToken(token)
    if not tokenValidator[0]:
        return {"error": "UnauthorizedError"}, 401
    else:
        return {
            "list": json.loads(tokenValidator[1].to_json())["my_collections"]
        }, 200


def delete_collection(token, collection_name):
    tokenValidator = validateToken(token)
    if not tokenValidator[0]:
        return {"error": "UnauthorizedError"}, 401
    else:
        user = tokenValidator[1]
        new_coll = []
        for i in user.my_collections:
            if i.collection_name != collection_name:
                new_coll.append(i)
        user.update(set__my_collections=new_coll)
        return {"message": "CollectionDeletedSuccesfully"}, 200


def update_collection(token, collection_name_list, product_id):
    tokenValidator = validateToken(token)
    if not tokenValidator[0]:
        return {"error": "UnauthorizedError"}, 401
    else:
        user = tokenValidator[1]
        k = list(set(collection_name_list))
        my_updated_collections = user.my_collections
        for i in k:
            if i not in my_updated_collections:
                create_collection(token, i)
            my_updated_collections[
                my_updated_collections.index(i)
            ].collection_item_list.append(product_id)
        return {"message": "ItemAddedSuccessfully"}, 200
