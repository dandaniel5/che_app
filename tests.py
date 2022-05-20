import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
import bson.json_util

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.TestUser

users = db.TestUsers
calendar = db.TestUsers.calendar

users.insert_one({"id": 219045984})
calendar.insert_one({"id": 219045984})



# collll = db.users.find_one({"_id" : ObjectId("627d59587b2c7be381050428")})
# def find_by_user_id(id):
#     user = db.users
#     cursor = col.find({"id": id})
#     list_cur = list(cursor)
#     json_data = dumps(list_cur)
#     # print(json_data)
#     return json_data


# data_user = {find_by_user_id(1)}
# print(data_user)
#
# print(find_by_user_id(222))
