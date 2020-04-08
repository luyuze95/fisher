# -*- coding: UTF-8 -*-
# @Time    : 2020/3/26 8:43 下午 
# @Author  : luYuZe
# @File    : gift.py 
# @Project : fisher
from collections import namedtuple

from app.view_models.book import BookViewModel

# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])
from app.view_models.gift import MyGifts


class MyWishes(MyGifts):
    pass
