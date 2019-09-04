# -*- coding: utf-8 -*-

# @File    : 邮件功能测试.py
# @Date    : 2019-08-22
# @Author  : litao
# @Describe:

from flask import Flask
from flask_mail import Mail, Message
import os
app = Flask(__name__)



MIME_TYPE = {
        '.xls':  'application/vnd.ms-excel',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        '.txt':  'text/plain',
        '.pdf':  'application/pdf',
        '.doc':  'application/msword',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        '.ppt':  'application/vnd.ms-powerpoint',
        '.rar':  'application/rar',
        '.zip':  'application/zip',
        '.tar':  'application/x-tar',
        '.gz':   'application/x-gzip'
    }
#配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '18301411335@qq.com',
    MAIL_PASSWORD = 'ewwtmbdaihzihehb', # this is email password(这是什么?下面会讲)
    FLASKY_MAIL_SENDER = '18301411335@qq.com',  # this is sender
    FLASKY_ADMIN = '18301411335@qq.com',  # this is the email of admin
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]',  # this is subject of email we will send
    MIME_TYPE = MIME_TYPE
)


@app.route('/')
def sendEmail():
    '''To:must be a list'''

    # From填写的电子邮箱地址必须与前面配置的相同
    From = '18301411335@qq.com'
    # 目标邮箱地址，可以替换为自己的QQ邮箱地址
    To = ["2585441465@qq.com"]
    Subject = 'hello world'
    Body = 'Only a test.'
    Html = '<h1>test test test.</h1>'
    Attachments = ['/Users/litao/Develop/Github/MyWeb/space/ceshi.xlsx']
    msg = Message(Subject, sender=From, recipients=To)
    msg.body = Body
    msg.html = Html
    # for f in Attachments:
    #     with app.open_resource(f) as fp:
    #         msg.attach(filename=os.path.basename(f), data=fp.read(),
    #             content_type = 'application/octet-stream')

    mail = Mail(app)
    with app.app_context():
        mail.send(msg)
    return "Email send success!"

if __name__ == "__main__":
    app.run()