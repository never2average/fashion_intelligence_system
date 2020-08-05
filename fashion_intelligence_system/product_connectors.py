from models import Product
import json
from authorization import validateToken

def product_details(token, product_id, amount):
    tokenValidator = validateToken(token)
    if not tokenValidator[0]:
        return {"error": "UnauthorizedError"}, 401
    elif amount == "full":
        return Product.objects.get(id=product_id).to_json(), 200
    else:
        return Product.objects.get(id=product_id).only("img_url","product_url").to_json(), 200