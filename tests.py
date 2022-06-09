import pymongo
# from bson.objectid import ObjectId
# from bson.json_util import dumps
# import bson.json_util
import re

import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.Users

# print(str(datetime.datetime.date(datetime.datetime.date())))

import datetime
from datetime import date, timedelta

# NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
# print (NextDay_Date)

# zavtra=(str(datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(days=1))))
# day=(str(datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(days=0))))
# vchera=(str(datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(days=-1))))

day = '2022-06-12'
'2022, 6, 9'


def day_datatime(day):
    # dayy = day.replace('-',', ')
    dayy = day.split('-')
    # print(type(date(int(dayy[0]), (int(dayy[1])), int(dayy[2]))))
    return date(int(dayy[0]), (int(dayy[1])), int(dayy[2]))


yesterday = str(day_datatime(day) + datetime.timedelta(days=-1))
tomorrow = str(day_datatime(day) + datetime.timedelta(days=-1))

print(yesterday)
# print(date(day_datatime(day)))


# vchera = datetime.datetime(2022, 3, 1)
# vchera.strftime("%Y-%m-%d")
# from datetime import date, timedelta
# date1 = date(2011, 10, 10)
# date2 = date1 + timedelta(days=5)
# print (date2)

# def next_day(day):
#     print(str(datetime.datetime.date(day + datetime.timedelta(days=1))))
#
#
# def prev_day(day):
#     print(str(datetime.datetime.date(day + datetime.timedelta(days=-1))))
#
# today = str(datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(days=+1)))
# print(today)
#
# next_day(vchera)
# # prev_day(zavtra)

# function return day after date
