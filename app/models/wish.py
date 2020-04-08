# -*- coding: UTF-8 -*-
# @Time    : 2020/3/24 9:12 下午
# @Author  : luYuZe
# @File    : wish.py
# @Project : fisher
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = cls.query.filter_by(
            uid=uid, launched=False
        ).order_by(
            desc(cls.create_time)
        ).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1
        ).group_by(
            Gift.isbn
        ).all()  # count_list原始数据 : [(3, '9818431321'),(2,'9784132112')]
        return [{'count': count, 'isbn': isbn} for count, isbn in count_list]


