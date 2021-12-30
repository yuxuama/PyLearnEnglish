import pymongo

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
    
    def get(self, limit=int, theme=None):
        pipeline = []
        if theme is None or theme == "all":
            pipeline = [
                {"$sample": {"size": limit}}
            ]
        else:
            pipeline = [
                {"$match": {"theme": theme}},
                {"$sample": {"size": limit}}
            ]
        cur = self.collection.aggregate(pipeline=pipeline)
        return cur

    def get_themes(self):
        pipeline = [
            {'$group': {"_id": "$theme"}}
        ]
        cur = self.collection.aggregate(pipeline=pipeline)
        return cur