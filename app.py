# encoding: UTF-8
"""
分词服务
"""

from json import dumps
from jieba import cut
from flask import Flask, request

APP = Flask(__name__)
PORT = 5000

@APP.route('/cut', methods=['POST'])
def cut_default():
    """
    默认分词模式
    """
    text = request.form['text']
    return dumps({'text': text, 'words': list(cut(text, cut_all=False))}, ensure_ascii=False)


@APP.route('/cut_all', methods=['POST'])
def cut_all():
    """
    全分词模式
    """
    text = request.form['text']
    return dumps({'text': text, 'words': list(cut(text, cut_all=True))}, ensure_ascii=False)

if __name__ == '__main__':
    APP.run(port=PORT)
