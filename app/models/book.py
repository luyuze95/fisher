# -*- coding: UTF-8 -*-
# @Time    : 2020/3/23 8:46 下午
# @Author  : luYuZe
# @File    : book.py
# @Project : fisher
from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    _author = Column('author', String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
