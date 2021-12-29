import pymongo

from pymongo import MongoClient
from os import environ

def get_database():
    # Connect to mongodb using pymongo
    CONNECTION_STRING = environ['MONGO_URL']

    TLS_FILE = environ['TLS_FILE_PATH']

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING, tls=True, tlsCAFile=TLS_FILE)
    # client = MongoClient(CONNECTION_STRING)

    database = client[environ['MONGO_DBNAME']]

    return database