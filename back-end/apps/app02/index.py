# -*- coding: utf-8 -*-

# @File    : index.py
# @Date    : 2019-08-21
# @Author  : litao
# @Describe:

from flask import Blueprint
from flask_cors import cross_origin

app02=Blueprint('app02',__name__)

@app02.route('/',methods=['GET'])
@cross_origin()
def show():
    return 'app02.hello'