from jieba import cut
from flask import Flask, request
from json  import dumps

ts = Flask(__name__)

@ts.route('/cut', methods=['POST'])
def cut_default():
    text = request.get_json(force=True)['text']
    return dumps({'text': text, 'words': list(cut(text, cut_all=False))}, ensure_ascii=False)

@ts.route('/cut_all', methods=['POST'])
def cut_all():
    text = request.get_json(force=True)['text']
    return dumps({'text': text, 'words': list(cut(text, cut_all=True))}, ensure_ascii=False)

ts.run(port=5000)
