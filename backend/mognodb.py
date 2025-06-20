from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insertEmbedding(obj):
    collection.insert_one(obj);

def fetchEmbedding():
    return collection.find({}, {"_id": 0, "content": 1, "embedding": 1})

