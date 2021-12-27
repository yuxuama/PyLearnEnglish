from db import Database
from flask.json import jsonify

db = Database()
cur = db.get(2)

resp = list(cur)
print(resp)
for element in resp:
    element.pop('_id', None)
print(resp)
print(jsonify(resp))