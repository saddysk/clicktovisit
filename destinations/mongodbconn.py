from pymongo import MongoClient

client = MongoClient("mongodb+srv://AK:okay@cluster0.smdfz.mongodb.net/HotelDestinationPage?retryWrites=true&w=majority")
db = client.get_database("HotelDestinationPage")
collection = db.hotels

def fetch_All():
    if collection is None:
        return None
    else:
        alldestinations = collection.find({})
        des = []
        for x in alldestinations:
            des.append(x)
        return des

