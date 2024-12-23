from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

client = MongoClient()

"""
    NOTE: Mongo client ip access list currently set to be accessible anywhere.
     I've done this for development purposes but before we push to prod it should be set to a static IP.

"""

USERNAME = os.environ["MONGO_USERNAME"]
PASSWORD = os.environ["MONGO_PASSWORD"]
URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster1.nfvpz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"


def connector():
    # Create a new client and connect to the server
    client = MongoClient(URI, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client.db
    except Exception as e:
        print(e)
        return None
    
def test_collection():
    database = connector()
    print(database.list_collection_names())
    print(database.users.find_one({"name":"Sean Brown"}))
