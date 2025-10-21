# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/21 22:32
"""
from src.models.user import User


class UserBase:
    """
    用户基础信息
    """
    @classmethod
    def create_user(cls,username,password,email="",phone_number="",nick_name=""):
        """
        创建用户
        :param username: 用户名
        :param password: 密码
        :param email: 邮箱
        :param phone_number: 手机号
        :param nick_name: 昵称
        :return:
        """
        if not nick_name:
            nick_name = username
        return User(username=username,
                    password=password,
                    email=email,
                    phone_number=phone_number,
                    nick_name=nick_name)




def main():
    pass


if __name__ == "__main__":
    main()
