from dataclasses import dataclass, field
from pydantic import BaseModel, ValidationError, fields
from bson.json_util import dumps, ObjectId
import json, os
from pymongo import MongoClient,errors

os.environ['MONGODB_URI'] = 'mongodb://localhost:27017/'
client = MongoClient(os.environ['MONGODB_URI'])
db = client.che_app

#
# def find_by_user_id(id):
#     col = db.Users
#     cursor = col.find({"id": id})
#     # list_cur =
#     for cu in cursor:
#         list_cur = cu
#     json_data = dumps(list_cur)
#     # print(json_data)
#     return json_data


# class Checkbox(BaseModel):
#     name: str = None
#     vall: str = None
#
# class Users(BaseModel):
#     _id: ObjectId
#     calendar: dict = None
#     id: str


# data_user = find_by_user_id(222)
# try:
#     danil = Users.parse_raw(find_by_user_id(219045984))
#     # print(danil.days[0].date)
#     days = list(danil.days)
#     for day in days:
#         print("88")
#     # print(days)
# except ValidationError as e:
#     print(e)

# print(data_user)
days = {'conect css': 'unchecked'}, {'conect jbl': 'unchecked'}, {'random text 3': 'unchecked'}
date = {"date": '2019-01-02'}
user_id ={ "id": "219045984"}
xxx = (json.dumps(days))

# col = db.users
# cursor = col.find(id)
# list_cur = col.find(id, date)
# print(list(list_cur.days.checkboxes))
#
#
# # col.find_one_and_replace({"id": "219045984", "data": date}, {"checkboxes": xxx})
# x=col.find({"id": 219045984})
# cursor =

date = "2022-04-18"
cursor = list((db.Users.find({"id": "219045984"},
                             {"id": 0, "_id": 0})))
for cu in cursor:
    calendar = cu
x = (calendar[date])
print((x))

list_val = []
for checkbox in x:
    # print({checkbox['name']}, {checkbox['vall']})
    list_val.append({f'{checkbox["name"]}': f'{checkbox["vall"]}'})
# print(len(list_val))
# print(x)

bb = "219045984"

try:
    db.Users.find_one_and_update({"id": bb}, {"$set": {date: "yzvyzv"}})
except Exception as e:
    print(e)