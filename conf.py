from pymongo import MongoClient
from settings import MONGO_URI


def mongo_conn():
    client = MongoClient(MONGO_URI)
    db = client["akg"].passwords
    return db
