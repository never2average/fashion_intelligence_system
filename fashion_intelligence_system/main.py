from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_cors import CORS
import mongoengine
from authorization import signup, login
from addwebsite import add_website
from collection import create_collection, list_collection
from collection import delete_collection, update_collection
from collection import list_collection_items, delete_collection_items
from product_connectors import product_details
from search import search, search_metadata, search_results

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
mongoengine.connect('FIS')

@app.route("/")
def main():
    return "API is up and running correctly"

class Signup(Resource):
    def post(self):
        request_data = request.get_json()
        email_id = request_data["email_id"]
        password = request_data["password"]
        first_name = request_data["firstname"]
        last_name = request_data["lastname"]
        return make_response(signup(email_id, password, first_name, last_name))


class Login(Resource):
    def post(self):
        request_data = request.get_json()
        email_id = request_data["email_id"]
        password = request_data["password"]
        return make_response(login(email_id, password))


class AddWebsite(Resource):
    def post(self):
        website_name = request.args.get("website")
        website_type = request.args.get("type")
        return make_response(add_website(website_name, website_type))


class CreateCollection(Resource):
    def post(self):
        jwt_token = request.headers.get("Authorization")
        collection_name = request.args.get("collection_name")
        return make_response(create_collection(jwt_token, collection_name))

class ListCollection(Resource):
    def get(self):
        jwt_token = request.headers.get("Authorization")
        return make_response(list_collection(jwt_token))


class UpdateCollection(Resource):
    def put(self):
        jwt_token = request.headers.get("Authorization")
        collection_list = request.get_json()["collection_names"]
        pid = request.args.get("item_id")
        return make_response(
            update_collection(jwt_token, collection_list, pid)
        )

class DeleteCollection(Resource):
    def delete(self):
        jwt_token = request.headers.get("Authorization")
        collection_name = request.args.get("collection_name")
        return make_response(delete_collection(jwt_token, collection_name))


class ListCollectionItems(Resource):
    def get(self):
        jwt_token = request.headers.get("Authorization")
        collection_name = request.args.get("collection_name")
        return make_response(
            list_collection_items(jwt_token, collection_name)
        )


class DeleteCollectionItems(Resource):
    def delete(self):
        jwt_token = request.headers.get("Authorization")
        collection_name = request.args.get("collection_name")
        product_id = request.args.get("product_id")
        return make_response(
            delete_collection_items(jwt_token, collection_name, product_id)
        )


class ProductDetails(Resource):
    def get(self):
        product_id = request.args.get("product_id")
        amount= request.args.get("amount")
        return make_response(product_details(product_id, amount))


class CreateSearch(Resource):
    def get(self):
        search_text = request.args.get("text")
        result_type = request.args.get("result_type")
        return make_response(search(search_text, result_type))


class SearchMetadata(Resource):
    def get(self):
        search_id = request.args.get("search_id")
        return make_response(search_metadata(search_id))


class SearchResults(Resource):
    def get(self):
        search_id = request.args.get("search_id")
        pageno = request.args.get("pageno")
        return make_response(search_results(search_id, pageno))


api.add_resource(Signup, "/signup")
api.add_resource(Login, "/login")
api.add_resource(ProductDetails, "/product/details")
api.add_resource(AddWebsite, "/toscrape")
api.add_resource(CreateCollection, "/collections/create")
api.add_resource(ListCollection, "/collections/list")
api.add_resource(UpdateCollection, "/collections/update")
api.add_resource(DeleteCollection, "/collections/delete")
api.add_resource(ListCollectionItems, "/collections/items/list")
api.add_resource(DeleteCollectionItems, "/collections/items/delete")
api.add_resource(CreateSearch, "/search_db")
api.add_resource(SearchMetadata, "/results/metadata")
api.add_resource(SearchResults, "/results")
if __name__ == "__main__":
    app.run(port=5000, debug=True)
