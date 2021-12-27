import pymongo
from pymongo.message import delete

class Database:

    def __init__(self) -> None:
        client = pymongo.MongoClient("mongodb+srv://yuxuama:8yy4MqY4@cluster0.n2tqt.mongodb.net/Database?retryWrites=true&w=majority")
        self.database = client.vocabulary
        self.collection = self.database.vocab

    def insert_word(self, word, trad, theme):
        self.collection.insert_one({
            "word": word,
            "trad": trad,
            "theme": theme
        })
    
    def delete(self, word=str):
        self.collection.delete_one({"word": word})
    
    def get(self, limit, theme=None):
        if theme is None:
            return self.collection.find({}).limit(limit)
        else:
            return self.collection.find({"theme": theme}).limit(limit)
    
    def get_themes(self):
        pipeline = [
            {'$group': {"_id": "$theme"}}
        ]
        cur = self.collection.aggregate(pipeline=pipeline)
        return cur