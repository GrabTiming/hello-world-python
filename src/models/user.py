# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/19 22:23
"""
from datetime import datetime
from sqlalchemy import  Column, Integer, String, DateTime
from src.models import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)
    nick_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now)



