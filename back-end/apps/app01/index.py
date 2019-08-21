# -*- coding: utf-8 -*-

# @File    : index.py.py
# @Date    : 2019-08-21
# @Author  : litao
# @Describe:

from flask import Blueprint,jsonify
from flask_cors import cross_origin

app01=Blueprint('app01',__name__)

@app01.route('/',methods=['GET'])
@cross_origin()
def show():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)