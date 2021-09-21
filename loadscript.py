import pymongo
import os
import json
from copy import deepcopy


from pymongo import collection
my_client = pymongo.MongoClient(os.environ.get('MONGO_CLIENT'))
colec = my_client['onboarding']['recipes_recipe']

# my_client.drop_database('onboarding')

with open('ablabla.json', 'r') as file:
    aa = json.load(file)
    colec.insert_many(list(aa))