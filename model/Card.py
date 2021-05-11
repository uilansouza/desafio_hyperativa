from model import Mongo


class Card:
    def __init__(self):
            """ Access Colection User
            """
            conn = Mongo()
            self.db = conn.db()
            self.table = self.db.card

    def insert_card(self, data):
     return  self.table.insert_one(data).inserted_id

    def find_card(self, data):
        return self.table.find_one(data)

