import pymongo
from pymongo import MongoClient

db = MongoClient("localhost")["crowdsource"]
topics_db = db.topics
label_db = db.labels
user_db = db.users
protected_collections = ["topics", "users", "label"]