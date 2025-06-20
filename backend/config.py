import os

OPENAI_API_KEY = ""
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "creerinfotech_db"
COLLECTION_NAME = "embedding"