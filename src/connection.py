from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://marcoaurelioo034:saZytW1QfNPfv7Ig@cluster0.dwlqu6z.mongodb.net/"
)

db = client.dio_livre

trends_collection = db.trends
