# -*- coding: utf-8 -*-

# @File    : main.py
# @Date    : 2019-08-21
# @Author  : litao
# @Describe:
from flask import Flask
from apps.app01.index import app01
from apps.app02.index import app02
app = Flask(__name__)

app.register_blueprint(app01)
app.register_blueprint(app01,url_prefix='/getMsg')
app.register_blueprint(app02,url_prefix='/app02')



if __name__ == '__main__':
    app.run(debug=True)