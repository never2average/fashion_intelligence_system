import json
from models import Website


def add_website(website_name, website_type):
    if website_type=="M" or website_type=="E":
        try:
            Website(
                website_name=website_name,
                website_type=website_type
            ).save()
            return json.dumps({"message": "AddingWebsiteSuccesful"}), 200
        except:
            return json.dumps({"message": "AddingWebsiteFailed"}), 401
    else:
        return json.dumps({"message": "AddingWebsiteFailed"}), 401