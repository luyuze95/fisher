# -*- coding: UTF-8 -*-
# @Time    : 2020/3/17 7:59 下午
# @Author  : luYuZe
# @File    : helper.py
# @Project : fisher


def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10 and word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
