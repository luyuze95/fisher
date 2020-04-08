# -*- coding: UTF-8 -*-
# @Time    : 2020/3/17 8:08 下午
# @Author  : luYuZe
# @File    : httper.py
# @Project : fisher
import requests


class HTTP(object):

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
