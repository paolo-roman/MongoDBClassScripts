import datetime   # This will be needed later
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from a .env file:
load_dotenv()
MONGODB_URI = 'mongodb+srv://pdromangarcia:BxBaNnIKNzBtrf1N@cluster0.tdsega9.mongodb.net/'

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
print('List of all databases in the cluster')
for db_info in client.list_database_names():
   print(db_info)
print('')


# Get a reference to the 'sample_mflix' database:
db = client['sample_mflix']

# List all the collections in 'sample_mflix':
print('List of all collections in sample_mflix')
collections = db.list_collection_names()
for collection in collections:
   print(collection)
print('')


# Import the `pprint` function to print nested data:
from pprint import pprint

# Get a reference to the 'movies' collection:
movies = db['movies']

# Get the document with the title 'Blacksmith Scene':
print('Find a movie')
pprint(movies.find_one({'title': 'Titanic'}))
print('')