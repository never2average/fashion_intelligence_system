from models import Product
import json
from authorization import validateToken


def product_details(product_id, amount):
    if amount == "full":
        return Product.objects.get(id=product_id).to_json(), 200
    else:
        return Product.objects.get(id=product_id).only(
            "img_url","product_url"
        ).to_json(), 200