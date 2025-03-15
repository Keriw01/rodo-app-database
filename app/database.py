from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# Pobierz dane z zmiennych środowiskowych
mongo_uri = os.getenv("MONGO_URI")

# Połączenie z MongoDB
client = MongoClient(mongo_uri)
db = client["dokumenty"]
collection = db["kolekcja"]
