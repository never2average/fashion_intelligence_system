from models import User
import jwt
import json
import base64
from datetime import datetime
from keys import secret_key
import bcrypt


def signup(email, password, firstname, lastname):
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    new_customer = User(firstname, lastname, email, password)
    try:
        new_customer.save()
        return json.dumps({
            "message": "SignupSuccessful",
            "Authorization": "Bearer %s" % base64.b64encode(
                jwt.encode({
                    "emailID": email,
                    "dt": datetime.now().strftime("%s")
                }, secret_key))
        }), 200
    except:
        return json.dumps({"message": "SignupFailed"}), 401


def login(email, password):
    try:
        user = User.objects.get(emailid=email)
        if bcrypt.checkpw(password, user.password):
            return json.dumps({
                "message": "LoginSuccessful",
                "Authorization": "Bearer %s" % base64.b64encode(
                    jwt.encode({
                        "emailID": email,
                        "dt": datetime.now().strftime("%s")
                    }, secret_key))
            }), 200
        else:
            return json.dumps({"message": "LoginFailed"}), 401
    except:
        return json.dumps({"message": "LoginFailed"}), 401