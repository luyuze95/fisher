# -*- coding: UTF-8 -*-
# @Time    : 2020/3/16 8:25 下午
# @Author  : luYuZe
# @File    : fisher.py
# @Project : fisher
from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=8000)
