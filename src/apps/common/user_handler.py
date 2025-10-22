# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/19 22:16

用户管理

"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.apps.common.user_base import UserBase
from src.db import get_db
from src.models.user import User
from src.schemas.dto.user_dto import UserRegister, UserUpdateDTO

user_router = APIRouter()

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_user(self, user: UserRegister):
        existing_user = self.db.query(User).filter(User.username == user.username).first()

        if existing_user:
            return {"message": "用户已存在"}

        new_user = UserBase.create_user(username=user.username, password=user.password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return {"message": "用户创建成功"}

    def get_user(self, username: str):
        user = self.db.query(User).filter(User.username == username).first()
        return user

    def update_user(self, user: UserUpdateDTO):
        username = user.username
        target_user = self.db.query(User).filter(User.username == username).first()

        if not target_user:
            return False

        target_user.username = user.username
        target_user.password = user.password if user.password else target_user.password
        target_user.email = user.email if user.email else target_user.email
        target_user.phone_number = user.phone_number if user.phone_number else target_user.phone_number
        target_user.nick_name = user.nick_name if user.nick_name else target_user.nick_name

        self.db.commit()
        self.db.refresh(target_user)
        return True

    def delete_user(self,username:str):
        target_user = self.db.query(User).filter(User.username == username).first()

        if not target_user:
            return False
        self.db.delete(target_user)
        self.db.commit()
        return True


@user_router.post("/register")
async def create_user(user:UserRegister,service: UserService =Depends()):
    return service.create_user(user)

@user_router.get("/get_user")
async def get_user(username: str, db: Session = Depends(get_db)):

    user_info = db.query(User).filter(User.username == username).first()

    result_data = {
        "username": user_info.username,
        "email": user_info.email,
        "phone_number": user_info.phone_number,
        "nick_name": user_info.nick_name
    }

    return {"msg":"","data": result_data,"code": 200}

@user_router.post("/update")
async def get_user(update_info: UserUpdateDTO, service: UserService = Depends()):

    print(update_info)
    success = service.update_user(update_info)

    return {"msg": "更新成功" if success else "更新失败", "code": 200 if success else 501}




def main():
    pass


if __name__ == "__main__":
    main()
