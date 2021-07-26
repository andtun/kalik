# This Python file uses the following encoding: utf-8

import markovify
from bottle import *

with open("kalik.txt", encoding='utf8') as f:
    text = f.read()

easy = markovify.Text(text, state_size=2, well_formed=False)
hard = markovify.Text(text, state_size=3, well_formed=False)

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

@post("/")
def new_kalik_text():
    return gen_kalik(easy)

@post("/hard")
def new_kalik_text():
    return gen_kalik(hard, minw=25)

@get("/main_files/<filename>")
def any_file(filename):
    return static_file(filename, root='./main_files')

# run the server
run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
