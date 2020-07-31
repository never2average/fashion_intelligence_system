from models import User
import jwt
import json
import base64
from datetime import datetime
from keys import secret_key
import bcrypt


def signup(email, password, firstname, lastname):
    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(
        firstname=firstname,
        lastname=lastname,
        emailid=email,
        password=password
    )
    try:
        new_user.save()
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
        if bcrypt.checkpw(password.encode('utf-8'), user.password):
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