from pymongo import MongoClient
from db_config import MONGO_URI  # Import the connection string

client = None
db = None

try:
    # Connect to the MongoDB server using the URI from db_config.py
    client = MongoClient(MONGO_URI)
    # Select the database. If it doesn't exist, create it on first document insertion
    db = client.inventory

    categories = db.category.find()

    # Print out each category
    for category in categories:
        print(category)

except Exception as e:
    print(e)

finally:
    if client is not None:
        client.close()
