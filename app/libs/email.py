# -*- coding: UTF-8 -*-
# @Time    : 2020/3/30 7:53 下午 
# @Author  : luYuZe
# @File    : email.py 
# @Project : fisher
from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_SENDER'], recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
