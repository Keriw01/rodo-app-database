from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["dokumenty"]
collection = db["kolekcja"]
