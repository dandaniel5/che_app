from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sslify import SSLify
import requests, json, os
from bson.json_util import dumps, ObjectId
import re
import datetime
from pydantic import BaseModel, Field, ValidationError
from pymongo import MongoClient

TOKEN = '5320542317:AAEd4A4lsBXyzYPXcl6ubw2j-mdVZz1rbj0'
HOOKURL = 'https://api.telegram.org/bot' + TOKEN + '/'
game_url = "https://c0fc-2a01-540-9e9-b400-ec76-9ae0-4a10-d354.ngrok.io"
game_short_name = 'checklist'
r = json

app = Flask(__name__)
SSLify = SSLify(app)
today = str(datetime.datetime.date(datetime.datetime.today()))

os.environ['MONGODB_URI'] = 'mongodb://localhost:27017/'
client = MongoClient(os.environ['MONGODB_URI'])
db = client.che_app


# def find_by_user_id(id):
#     col = db.users
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


# class Users(BaseModel):
#     _id: ObjectId
#     id: str


# def get_days_by_user_id(id):
#     user = Users.parse_raw(find_by_user_id(id))
#     return (user.days)


# try:
#     danil = Users.parse_raw(find_by_user_id(219045984))
#     print(danil.days[0].date)
# except ValidationError as e:
#     print(e)
welcome_checkbox1 = {"name": "просто новый создан день", "vall": "unchecked"}
welcome_checkbox2 = {"name": "значть можно поставить галочку", "vall": "checked"}
welcome_checkbox3 = {"name": "RANDOM TEXT3", "vall": "checked"}
new_day = (welcome_checkbox1, welcome_checkbox2, welcome_checkbox3)


def is_user_exist(user_id):
    if db.Users.find_one({"id": f"{user_id}"}) != None:
        return True
    else:
        return False


def is_date_exist(user_id, date):
    # date = str(date)
    print(f"{date=}" + f"{user_id=}")
    dates = db.Users.find_one({"id": f"{user_id}"},
                              {"id": 0, "_id": 0})  # получаем все даты пользователя или нихуя если пользоватекля нема
    if dates != None:
        print(dates)
        if date in list(dates.keys()):
            print("date exist")
            return True
        elif date not in list(dates.keys()):
            print("is_date_exist date not exist")
            return False
    else:
        print("user not found")
        return None
        # false if user dont exist


def init_date(user_id, date):
    print("init_date")
    print(user_id)
    print(date)

    db.Users.update_one({"id": str(user_id)}, {"$set": {date: new_day}})
    print("date created")


def init_user(user_id):

    welcome_checkbox1 = {"name": "welcome to checkbox_app", "vall": "unchecked"}
    welcome_checkbox2 = {"name": "use it to checkbox your ass", "vall": "checked"}
    welcome_checkbox3 = {"name": "RANDOM TEXT3", "vall": "unchecked"}
    new_user_day = (welcome_checkbox1, welcome_checkbox2, welcome_checkbox3)

    match is_user_exist(user_id):
        case False:  # if user does not exist create new user and new user day
            db.Users.insert_one({"id": f"{user_id}", today: new_user_day})
            print("user created")
            print("date also created")
        case True:  # if user exist check if date exist if not create new date(today)
            print("user exist")
            match is_date_exist(user_id, today):
                case None:
                    print("user not found")
                case True:
                    print("is_date_exist date exist")
                case False:
                    print("date not exist")
                    init_date(user_id, today)
            print("today date created")


def sendgame(chat_id, user_id):
    init_user(user_id)
    print('send gamestarted')
    qqurl = HOOKURL + 'sendGame'
    answer = {'chat_id': chat_id, 'game_short_name': game_short_name, 'cache_time': 20}
    print(qqurl)
    requests.post(qqurl, json=answer)
    print('send game done')
    return (user_id)


def sendGameUrl(callback_query_id, user_id, date):
    init_user(user_id)
    qurl = HOOKURL + 'answerCallbackQuery'
    print("sendGameUrl_user_id: ", user_id)
    URL_GAME = game_url + f'/gm/{user_id}/{date}/'
    answer = {'callback_query_id': callback_query_id, 'url': URL_GAME}
    print('answer=', answer)
    requests.post(qurl, json=answer)
    return (user_id)


def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count


@app.route('/chb', methods=['POST'])
def front_to_back():
    print('/chb')
    jj = request.get_json()
    print(jj)
    id, date, *checkboxes = jj
    print(f'{id=},{date=},{checkboxes=}')
    checkboxes_4_mongo = []
    for x in range(0, len(checkboxes), 2):
        checkboxes_4_mongo.append({'name': checkboxes[x], 'vall': checkboxes[x + 1]})
    print(checkboxes_4_mongo)
    # dayz=[]
    # for y in range(0, len(day),2):
    #     dayz.append({day[y]: day[y+1]})
    # print(dayz)
    db.Users.update_one({"id": f"{id}"}, {"$set": {f"{date}": checkboxes_4_mongo}})
    # db.Users.find_one_and_update({"id": f"{jj[0]}"}, {"$set": {f"{jj[1]}": day}})
    print('ok')
    return jsonify({"status": "nice"})

    # @app.route('/gm', methods=['GET', 'POST'])
    # def send_json_to_front():
    #     with open("data.json") as jsonFile:
    #         jsonObject = json.load(jsonFile)
    #         jsonFile.close()
    #     return render_template('index.html', list_val=jsonObject, list_val_len=len(jsonObject))


@app.route('/gm/<int:user_id>/<string:date>/', methods=['GET', 'POST'])
def send_json_to_front_from_mongo_by_user_id_and_date(user_id, date):
    print('-----------------')
    cursor = list((db.Users.find({"id": f"{user_id}"},
                                 {"id": 0, "_id": 0})))
    for cu in cursor:
        calendar = cu
    x = (calendar[date])
    print(x)

    dates = re.findall(r'\d{4}-\d{2}-\d{2}', str(db.Users.find_one({"id": f"{user_id}"}, {"id": 0, "_id": 0})))
    print(dates)

    try:
        if date in dates:
            print('date in dates')
            print(date)
    except:
        print('date not in dates')
        print(date)
        return jsonify({"status": "not_found"})

    list_val = []
    for checkbox in x:
        print({checkbox['name']}, {checkbox['vall']})
        list_val.append({f'{checkbox["name"]}': f'{checkbox["vall"]}'})

    # user = Users.parse_raw(find_by_user_id(user_id))
    # print('user=', user)
    # days = list(get_days_by_user_id(user_id))
    # print(f'{days=}')
    # for day in days:
    #     print(f'{day=}')
    #     if day.date == date:
    #         fdate = day.date
    #         print(f'{fdate=}')
    #         checkboxes = day.checkboxes
    # print(f'{checkboxes=}')
    # print('----------------')
    # # print(f'{checkboxes=}')
    # list_val = []
    # for checkbox in checkboxes:
    #     print({f'{checkbox.name}:{checkbox.vall}'})
    #     list_val.append({f'{checkbox.name}': f'{checkbox.vall}'})
    #
    # print(f'{list_val=}')
    #
    # # print(f'{fdate=}')
    # # print(list(day.checkboxes))
    # # print(len(days))
    return render_template('index.html', list_val=list_val, list_val_len=len(list_val), dates=dates, date=date,
                           game_url=game_url, user_id=user_id)


@app.route('/', methods=['GET', 'POST'])
def index():
    print('START')
    # global r
    r = request.get_json()
    print(r)

    if request.method == 'POST':
        if 'callback_query' in r:
            print('send url')
            print(r)
            callback_query_id = r['callback_query']['id']
            print(callback_query_id)
            # update_id = r['update_id']
            user_id = int(r['callback_query']['from']['id'])
            # регуляркой дотсаем все даты из монго джейсона по юзер айди
            date = re.findall(r'\d{4}-\d{2}-\d{2}', str(db.Users.find_one({"id": f"{user_id}"}, {"id": 0, "_id": 0})))
            day = str(datetime.datetime.date(datetime.datetime.today()))
            sendGameUrl(callback_query_id, user_id, day)
            return jsonify({"status": "nice"})

        elif 'message' in r:
            if r['message']['text'] == '/start':
                chat_id = r['message']['chat']['id']
                print('send game')
                user_id = r['message']['from']['id']
                # print(r)
                # проверить есть ли юзер айди в базе , если нет то добавить и создать календарь
                # с сегодняшним днем и добавить в него первую записть "зарегаться в приложениии ЧЕКЕД"
                # и вторым чеклистом "Поставить первую галоку АНЧЕКЕД
                sendgame(chat_id, user_id)
    return render_template("base.html")


if __name__ == '__main__':
    wurl = HOOKURL + 'setWebhook?url=' + game_url
    Set = requests.get(wurl)
    print(Set)
    app.run(host="localhost", port=5003, debug=True)
