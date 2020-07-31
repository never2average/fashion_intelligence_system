from mongoengine import Document, EmbeddedDocument, IntField
from mongoengine import StringField, EmailField, BinaryField
from mongoengine import URLField, EmbeddedDocumentListField
from mongoengine import ListField, DictField


class Website(Document):
    website_name = URLField(required=True)
    website_type = StringField(required=True, choices=["M", "E"])


class Product(EmbeddedDocument):
    item_source = StringField(required=True, choices=["Maga", "Ecom", "Socl"])
    img_url = URLField(required=True)
    product_url = URLField(required=True)
    tags_list = ListField(StringField)
    sales_data = DictField()


class Collection(Document):
    collection_name = StringField(required=True)
    collection_item_list = EmbeddedDocumentListField(Product)


class User(Document):
    firstname = StringField(max_length=15, required=True)
    lastname = StringField(max_length=15)
    emailid = EmailField(required=True)
    password = BinaryField(required=True)
    my_collections = ListField(Collection)