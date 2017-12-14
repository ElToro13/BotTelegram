import json
import requests
import time
import urllib
import urllib.request
#from BrainFalcFury import data
import config
import random
from chatbotLayout import iinput
import os

TOKEN = "457762085:AAE9eFQrFHOq-OJoEyMLCx2O85kGpl3sEY4"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    try:
        for update in updates["result"]:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            text = iinput(text, chat)
            print(text)
            keyboard = build_keyboard()
            send_message(text, chat, keyboard)
    except Exception as e:
        print(e)
        
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def build_keyboard():
    keyboard = [['Cricket', 'Football'],
                ['Reminder', 'News', 'Dictionary'],
                ['/photo','Weather']]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)


def main():
    last_update_id = None
    print("Stage - 1")
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            print("Stage - 2")
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
