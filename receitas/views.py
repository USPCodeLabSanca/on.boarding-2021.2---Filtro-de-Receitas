from django.http import HttpResponse
import pymongo
# import os

# my_client = pymongo.MongoClient(os.getenv('ONBOARDING_DB'))
# colec = my_client['onboarding']['receitas']

# print(colec.find_one({}))

def index(request):
    return HttpResponse("Hello, world. You're at the index.")