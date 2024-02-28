from bson import ObjectId
from pymongo import MongoClient
from db_config import MONGO_URI  # Import the connection string

client = None
db = None

try:
    # Connect to the MongoDB server using the URI from db_config.py
    client = MongoClient(MONGO_URI)
    # Select the database. If it doesn't exist, create it on first document insertion
    db = client.inventory

    _id = input("Enter supplier id: ")

    # Find the supplier with the given id and convert the string input to an ObjectId
    supplier = db.supplier.delete_one({"_id": ObjectId(_id)})
    # If the item doesn't exist, raise an exception
    if supplier.deleted_count == 0:
        raise Exception("Supplier does not exist")

except Exception as e:
    print(e)

finally:
    if client is not None:
        client.close()
