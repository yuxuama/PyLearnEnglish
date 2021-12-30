from db import Database

db = Database()
cur = db.get(2, "theme1")

for element in cur:
    print(element)
