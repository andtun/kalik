# This Python file uses the following encoding: utf-8

import markovify
from bottle import *

with open("kalik.txt", encoding='utf8') as f:
    text = f.read()

text_model_2 = markovify.Text(text, state_size=2, well_formed=False)

def gen_kalik():
    res = None
    while res is None:
        res = text_model_2.make_sentence(min_words=35, max_words=100, tries=100)
    return res


@get("/")
def main():
    return static_file('Порфирьевич.htm', root='.')

@post("/")
def new_kalik_text():
    return gen_kalik()


# run the server
run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
