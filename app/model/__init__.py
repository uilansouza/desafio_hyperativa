import pymongo
import os


class Mongo:

    def db(self):
        try:
            MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')
            DBAAS_MONGODB_ENDPOINT = os.getenv('DBAAS_MONGODB_ENDPOINT')
            client = pymongo.MongoClient(DBAAS_MONGODB_ENDPOINT)
            return client[MONGODB_DATABASE]
        except Exception as e:
            print("error {}".format(str(e)))
            return str(e), 400


