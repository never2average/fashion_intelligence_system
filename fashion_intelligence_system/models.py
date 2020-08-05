from mongoengine import Document, IntField, EmbeddedDocument
from mongoengine import StringField, EmailField, BinaryField
from mongoengine import URLField, ListField, DictField
from mongoengine import EmbeddedDocumentListField


class Website(Document):
    website_name = URLField(required=True)
    website_type = StringField(required=True, choices=["M", "E"])


class Product(Document):
    item_source = StringField(required=True, choices=["Maga", "Ecom", "Socl"])
    img_url = URLField(required=True)
    product_url = URLField(required=True)
    tags_list = ListField(StringField)
    sales_data = DictField()
    product_description = StringField()
    trending_score = IntField(required=True, default=0)


class Collection(EmbeddedDocument):
    collection_name = StringField(required=True)
    collection_item_list = ListField(BinaryField)


class User(Document):
    firstname = StringField(max_length=15, required=True)
    lastname = StringField(max_length=15)
    emailid = EmailField(required=True, unique=True)
    password = BinaryField(required=True)
    my_collections = EmbeddedDocumentListField(Collection)