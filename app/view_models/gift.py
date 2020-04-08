# -*- coding: UTF-8 -*-
# @Time    : 2020/3/26 8:43 下午 
# @Author  : luYuZe
# @File    : gift.py 
# @Project : fisher
from collections import namedtuple

from app.view_models.book import BookViewModel

# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts(object):

    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # return my_gift
        r = {
            'wishes_count': count,
            'book': BookViewModel(gift.book),
            'id': gift.id
        }
        return r
