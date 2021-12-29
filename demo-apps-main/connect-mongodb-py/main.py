import datetime

from dotenv import load_dotenv
from db_connection import get_database
from os import environ

# Load environment variables from .env
load_dotenv()


# Get the last date when a publication was extracted
def get_data():
    database = get_database()

    # Select collection
    collection_name = environ['COLLECTION_NAME']
    collection = database[collection_name]

    # Get all docs
    res = collection.find({})
    
    # Close database connection
    database.client.close()

    # Returns first item
    return res[0]

def insert_data(json_object):
    # Create DB Client
    database = get_database()                           

    # Select collection
    collection_name = environ['COLLECTION_NAME']
    collection = database[collection_name]

    # Insert new item
    insert_result = collection.insert_one(json_object)  
    
    # Close database connection
    database.client.close()

    return insert_result                             


def main():
    # old_data = get_data()
    current_time = datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S GMT-3")

    json_object = {
        'current_time' : current_time
    }    

    result = insert_data(json_object)

    print('Successfully inserted new registry into database.\nRegistry ', json_object)

if __name__ == '__main__':
    main()                      # Run Main program
