from pymongo import MongoClient

client = MongoClient("mongodb+srv://AK:okay@cluster0.smdfz.mongodb.net/HotelDestinationPage?retryWrites=true&w=majority")
db = client.get_database("HotelDestinationPage")
collection = db.full_hotels

def fetch_one(id):
    if collection is None:
        return None
    else:
        alldestinations = collection.find_one({"id" : id})
        return alldestinations

def getRoomDetails(id , roomId):
    if collection is None:
        return None
    else:
        roomdetails = collection.find_one({"id" : id} , {"Rooms" : 1 , "_id" : 0})
        for room in roomdetails:
            if room.id == roomId:
                return room
        return None

