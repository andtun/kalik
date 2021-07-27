# This Python file uses the following encoding: utf-8

import vk_api
import markovify
from bottle import *

with open("kalik.txt", encoding='utf8') as f:
    text = f.read()

easy = markovify.Text(text, state_size=2, well_formed=False)
hard = markovify.Text(text, state_size=3, well_formed=False)

vk = vk_api.VkApi(token='4d0e510aa01f5bf9cb5e68d8620939d03f11b939347c58acdff5f123458e662b0eafae16f92f3038aa717') #Авторизоваться как сообщество

def write_msg(chat_id, s):
    vk.method('messages.send', {'chat_id':chat_id,'message':s, 'random_id':hash(s)})

def gen_kalik(model, minw=35):
    res = None
    while res is None:
        res = model.make_sentence(min_words=minw, max_words=100, tries=100)
    return res


@get("/")
def main():
    return static_file('main.htm', root='.')

@get("/favicon.ico")
def main_ico():
    return static_file('favicon.ico', root='.')

@get("/342")
def my_group():
    msg = gen_kalik(easy)
    write_msg(2, msg)
    return 0

@get("/342hard")
def my_group():
    msg = gen_kalik(hard, minw=25)
    write_msg(2, msg)
    return 0

@post("/")
def new_kalik_text():
    return gen_kalik(easy)

@post("/hard")
def new_kalik_text():
    return gen_kalik(hard, minw=25)

@post("/verify")
def verify():
    return "f78b12c7"

@get("/main_files/<filename>")
def any_file(filename):
    return static_file(filename, root='./main_files')

# run the server
run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
