from flask import json
from flask.helpers import url_for
from flask.json import jsonify
from flask.wrappers import Request
from db import Database
from flask import Flask, render_template, make_response, redirect, request

class Api:

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.db = Database()
    
    def set_route(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/get<int:size>', 'get', self.get_word, methods=['GET'])
        self.app.add_url_rule('/get/', 'get', self.get_word, methods=['GET'])
        self.app.add_url_rule('/get_theme', 'gettheme', self.get_theme, methods=['GET'])
        self.app.add_url_rule('/lesson?<int:n>&<string:theme>', 'lesson', self.lesson)
        self.app.add_url_rule('/lesson', 'lesson', self.lesson)
        self.app.add_url_rule('/submit', 'submit', self.submit, methods=['POST', 'GET'])

    def launch(self, host="127.0.0.1", port=8080):
        self.set_route()
        self.app.run(host=host, port=port)
    
    def get_word(self, size=1):
        cur = list(self.db.get(size))
        for element in cur:
            element.pop('_id', None)
        return jsonify(cur)
    
    def get_theme(self):
        data = list(self.db.get_themes())
        resp = {}
        for i in range(len(data)):
            resp[i] = data[i]['_id']
        return make_response(resp)

    def lesson(self, n=10, theme='all'):
        return render_template('lesson.html', n=n, theme=theme)

    def submit(self):
        print(request.json)
        return 'ok'

    def index(self):
        return render_template('index.html')


if __name__ == '__main__':
    api = Api()
    api.launch()
    