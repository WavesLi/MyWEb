# -*- coding: utf-8 -*-

# @File    : tmp.py
# @Date    : 2019-08-22
# @Author  : litao
# @Describe:

from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 127.0.0.1:5000/goods/110
# @app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")  # 不加转换器类型， 默认是普通字符串规则（除了/的字符）
def goods_detail(goods_id):
    """定义的视图函数"""
    return "goods detail page %s" % goods_id


# 1. 定义自己的转换器，第一种是普通的定义方式，regex属性正则规则必要的属性写死内部
class PhoneConverter(BaseConverter):
    def __init__(self, url_map):
        super(PhoneConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'


# 通用转换器的定义方式
class RegexConverter(BaseConverter):
    """"""

    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        """"""
        print("to_python方法被调用")
        # return "abc"
        # value是在路径进行正则表达式匹配的时候提取的参数
        return value

    def to_url(self, value):
        """使用url_for的方法的时候被调用"""
        print("to_url方法被调用")
        # return "15811111111"
        return value


# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] = PhoneConverter


# 127.0.0.1:5000/send/18612345678
# @app.route("/send/<mobile:mobile_num>")
@app.route("/send/<re(r'1[34578]\d{9}'):mobile_num>")
def send_sms(mobile_num):
    return "send sms to %s" % mobile_num


@app.route("/index")
def index():
    url = url_for("send_sms", mobile_num="18922222222")
    # /send/18922222222
    return redirect(url)


@app.route("/call/<re(r''):tel>")
def call_tel(tel):
    pass


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    # 启动flask程序
    app.run(debug=True)