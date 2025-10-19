# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/19 22:53
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from src.models import Base

username = "root"
password = "123456"
db_name = "hello-world"


# 生产环境推荐配置
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@localhost/{db_name}",
    poolclass=QueuePool,
    pool_size=10,           # 连接池大小
    max_overflow=20,        # 最大溢出连接数
    pool_pre_ping=True,     # 连接前ping检查
    pool_recycle=3600,      # 连接回收时间（秒）
    echo=False              # 是否输出SQL日志（生产环境设为False）
)

# 创建引擎和会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    # 确保模型被加载
    # 在函数内部导入，避免模块级循环导入
    from src.models.user import User
    from src.models import Base

    print("create table start ===================")
    print(f"Base metadata tables: {Base.metadata.tables}")
    Base.metadata.create_all(bind=engine)
    print("create table end ===================")

init_db()