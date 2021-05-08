from model import Mongo
from bson.objectid import ObjectId
import pytz
import os

class User:
    def __init__(self):
            """ Access Colection User
            """
            conn = Mongo()
            self.db = conn.db()
            self.table = self.db.user

    def insert_user(self, data):
     return  self.table.insert_one(data).inserted_id

    def find_user(self, data):
        return self.table.find_one(data)

