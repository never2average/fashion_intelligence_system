from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_cors import CORS
import mongoengine
from authorization import signup, login
from addwebsite import add_website


app = Flask(__name__)
cors = CORS(app)
api = Api(app)
mongoengine.connect('Jarvis')


class Signup(Resource):
    def post(self):
        email_id = request.get_json("email")
        password = request.get_json("password")
        first_name = request.get_json("firstname")
        last_name = request.get_json("lastname")
        return make_response(signup(email_id, password, first_name, last_name))


class Login(Resource):
    def post(self):
        email_id = request.get_json("email")
        password = request.get_json("password")
        return make_response(login(email_id, password))


class AddWebsite(Resource):
    def post(self):
        website_name = request.args.get("website")
        website_type = request.args.get("type")
        return make_response(add_website(website_name, website_type))


class CreateCollection(Resource):
    def post(self):
        collection_id = request.args.get("id")


class ListCollection(Resource):
    def get(self):
        collection_id = request.args.get("id")


class UpdateCollection(Resource):
    def put(self):
        collection_id = request.args.get("id")


class DeleteCollection(Resource):
    def delete(self):
        collection_id = request.args.get("id")


api.add_resource(Signup, "/signup")
api.add_resource(Login, "/login")
api.add_resource(AddWebsite, "/toscrape")
api.add_resource(CreateCollection, "/collections/create")
api.add_resource(ListCollection, "/collections/list")
api.add_resource(UpdateCollection, "/collections/update")
api.add_resource(DeleteCollection, "/collections/delete")
if __name__ == "__main__":
    app.run(port=5000, debug=True)
