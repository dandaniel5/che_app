from dataclasses import dataclass, field
from pydantic import BaseModel, ValidationError, fields
from bson.json_util import dumps, ObjectId
import json, os, re
import datetime
from pymongo import MongoClient, errors


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
# days = {'conect css': 'unchecked'}, {'conect jbl': 'unchecked'}, {'random text 3': 'unchecked'}
# date = {"date": '2019-01-02'}
# user_id = {"id": "219045984"}
# xxx = (json.dumps(days))

# col = db.users
# cursor = col.find(id)
# list_cur = col.find(id, date)
# print(list(list_cur.days.checkboxes))
#
#
# # col.find_one_and_replace({"id": "219045984", "data": date}, {"checkboxes": xxx})
# x=col.find({"id": 219045984})
# cursor =

# date = "2022-05-17"
# cursor = list((db.Users.find({"id": "219045984"},
#                              {"id": 0, "_id": 0})))
# for cu in cursor:
#     calendar = cu
# x = (calendar[date])
# print((x))
#
# list_val = []
# for checkbox in x:
#     # print({checkbox['name']}, {checkbox['vall']})
#     list_val.append({f'{checkbox["name"]}': f'{checkbox["vall"]}'})
# # print(len(list_val))
# # print(x)
#
#
# xx = [{'name': 'conect css', 'vall': 'unchecked'}, {'name': 'conect cggss', 'vall': 'unchecked'}]
#
# try:
#     db.Users.find_one_and_update({"id": "219045984"}, {"$set": {"2022-05-19": xx}})
#     # db.Users.find_one_and_update({"id": f"{jj[0]}" }, {"$set": {yy: day}})
# except Exception as e:
#     print(e)
user_id = "5197484110"
# date = db.Users.find_one({"id": f"{user_id}"}, {"id": 0, "_id": 0})
# print(date)
# data =[]
# for x in date:
#     data.append(x)
# print(data)
# date = re.findall(r'\d{4}-\d{2}-\d{2}', str(db.Users.find_one({"id": f"{user_id}"}, {"id": 0, "_id": 0})))
# print(date)


# def is_user_exist(user_id):
#     user = db.Users.find_one({"id": f"{user_id}"})
#     if user != None:
#         return user
#     else:
#         return False
#
# def is_date_exist_if_not_init(user_id, date):
#     dates = db.Users.find_one({"id": f"{user_id}"}, {"id": 0, "_id": 0}) # получаем все даты пользователя или нихуя если пользоватекля нема
#     if dates != None: #
#         for date in dates:
#             if date == date:
#                 return True
#                 print("date exist")
#             else:
#                 # creaate new day
#                 db.Users.insert_one({"id": f"{user_id}", date:({"checkboxes": [{"name": "new day", "vall": "cheked"}] }) })
#                 print("date created")
#     else:
#         return False # false if user dont exist
#
# def init_user(user_id):
#     today = str(datetime.datetime.date(datetime.datetime.today()))
#     welcome_checkbox1 = {"name": "welcome to checkbox_app", "vall": "unchecked"}
#     welcome_checkbox2 = {"name": "use it to checkbox your ass", "vall": "checked"}
#     welcome_checkbox3 = {"name": "RANDOM TEXT3", "vall": "unchecked"}
#     new_user_day = (welcome_checkbox1, welcome_checkbox2, welcome_checkbox3)
#
#     user_id = is_user_exist(user_id)# if user does not exist return False else return user
#
#     if user_id == False: # if user does not exist create new user and new user day
#         db.Users.insert_one({"id": f"{user_id}",today:new_user_day})
#         print("user created")
#         print("date also created")
#     else: # if user exist check if date exist if not create new date(today)
#         print("user exist")
#         is_date_exist_if_not_init(user_id, today)
#         print("today date created")


dates = (db.Users.find_one({"id": f"{user_id}"}, {"id": 0, "_id": 0}))
print(list(dates.keys()))
# print(re.match(r'\d{4}-\d{2}-\d{2}', dates)

# print(datetime.datetime.date(datetime.datetime.today()))
# today = datetime.datetime.today()
# print(re.match(r'\d{4}-\d{2}-\d{2}', str(today)))
# init_user(user_id)
