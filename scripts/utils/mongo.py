from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['movie_booking']

movie_collection = db['movie_collection']