from mongoengine import Document, EmbeddedDocument, IntField
from mongoengine import StringField, EmailField, BinaryField
from mongoengine import URLField, EmbeddedDocumentListField


class User(Document):
    firstname = StringField(max_length=10, min_length=10, required=True)
    lastname = StringField(max_length=10, min_length=10)
    emailid = EmailField(max_length=10, min_length=10, required=True)
    password = BinaryField(required=True)


class Website(Document):
    website_name = URLField(required=True)
    website_type = StringField(required=True, choices=["M", "E"])


class CollectionItem(EmbeddedDocument):
    pass


class Collection(Document):
    collection_id = IntField(required=True)
    collection_name = StringField(required=True)
    collection_list = EmbeddedDocumentListField(CollectionItem)