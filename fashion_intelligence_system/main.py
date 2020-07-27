from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import mongoengine

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
mongoengine.connect('Jarvis')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
