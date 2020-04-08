# -*- coding: UTF-8 -*-
# @Time    : 2020/3/24 9:12 下午
# @Author  : luYuZe
# @File    : gift.py
# @Project : fisher
from collections import namedtuple

from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = cls.query.filter_by(
            uid=uid, launched=False
        ).order_by(
            desc(cls.create_time)
        ).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1
        ).group_by(
            Wish.isbn
        ).all()  # count_list原始数据 : [(3, '9818431321'),(2,'9784132112')]
        return [{'count': count, 'isbn': isbn} for count, isbn in count_list]

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gift = cls.query.filter_by(
            launched=False
        ).group_by(
            cls.isbn
        ).order_by(
            desc(cls.create_time)
        ).limit(
            current_app.config['RECENT_BOOK_COUNT']
        ).distinct().all()
        return recent_gift


