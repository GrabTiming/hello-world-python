# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/16 21:11
"""
from fastapi import FastAPI
import src.db
# 创建 FastAPI 实例
app = FastAPI(
    title="我的API服务",
    description="这是一个演示用的API接口",
    version="1.0.0"
)


# 根路径接口
@app.get("/hello")
async def hello():
    return {
        "message": "欢迎来到hello-python项目",
        "status": "服务运行正常",
        "docs_url": "http://127.0.0.1:8000/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
