# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/20 23:40
"""
import re
from typing import Optional

from pydantic.v1 import BaseModel, validator


class UserRegister(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    phone: Optional[str] = None

    @validator('username')
    def validate_username(cls, v):
        if len(v) < 3 or len(v) > 20:
            raise ValueError('用户名长度必须在3-20个字符之间')
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('用户名只能包含字母、数字和下划线')
        return v

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('密码长度至少6位')
        return v

class UserUpdateDTO(BaseModel):
    username: str
    password: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    nick_name: Optional[str] = None


def main():
    pass


if __name__ == "__main__":
    main()
