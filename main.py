from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sslify import SSLify
import requests, json, os
import re
TOKEN = '5320542317:AAEd4A4lsBXyzYPXcl6ubw2j-mdVZz1rbj0'
HOOKURL = 'https://api.telegram.org/bot' + TOKEN + '/'
Game_url = "https://3fc9-2a01-540-853-4400-1427-c266-2897-ba20.ngrok.io"
game_short_name = 'checklist'
r = json

app = Flask(__name__)
SSLify = SSLify(app)


# @app.route('/', methods=['GET'])
# def index():
#     with open("data.json") as jsonFile:
#         jsonObject = json.load(jsonFile)
#         jsonFile.close()
#         print(jsonObject)
#
#     return render_template('index.html')


def sendGame(chat_id):
    print('send gamestarted')
    qqurl = HOOKURL + 'sendGame'
    answer = {'chat_id': chat_id, 'game_short_name': game_short_name, 'cache_time':20}
    print(qqurl)
    requests.post(qqurl, json=answer)
    print('send game done')


def sendGameUrl(callback_query_id):
    qurl = HOOKURL + 'answerCallbackQuery'
    URL_GAME = Game_url + '/gm'
    answer = {'callback_query_id': callback_query_id, 'url': URL_GAME}
    print('answer=', answer)
    requests.post(qurl, json=answer)

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

@app.route('/chb', methods=['POST'])
def readjson():
    jj = request.get_json()
    print(jj)
    jjj = []
    i = 0
    sss = (jj.count("checked")+jj.count("unchecked"))
    print(sss)
    for i in range(sss):
        print(i)
        ii = i*2
        ras = jj[ii]
        dva = jj[ii+1]
        dickt = {ras:dva}
        jjj.append(dickt)
    print(jjj)

    with open("data.json", "w") as j:
        json.dump(jjj, j)
        j.close()
    #
    # j = request.get_json()
    # print("json",json)
    # with open('data.json', 'w') as f:
    #     j.dump(j, f)
    #     f.close()
    return jsonify({"status": "nice"})

@app.route('/gm', methods=['GET', 'POST'])
def send_json_to_front():
    with open("data.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    return render_template('index.html', list_val=jsonObject, list_val_len=len(jsonObject))

@app.route('/', methods=['GET', 'POST'])
def index():
    print('START')
    global r
    r = request.get_json()
    print(r)
    if request.method == 'POST':

        if 'callback_query' in r:
            print('send url')
            callback_query_id = r['callback_query']['id']
            print(callback_query_id)
            update_id = r['update_id']
            sendGameUrl(callback_query_id)

        elif 'message' in r:
            if r['message']['text'] == '/start':
                chat_id = r['message']['chat']['id']
                print('send game')
                sendGame(chat_id)
    return render_template("base.html")


if __name__ == '__main__':
    # wurl = HOOKURL + 'setWebhook?url=' + Game_url
    # Set = requests.get(wurl)
    # print(Set)
    app.run(host="localhost", port=5003, debug=True)
