# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/16 22:15
"""
import io
from datetime import datetime

import pandas as pd

EXCEL_FILE_PATH_TEXT = "resource/excel_file_1.xlsx"
EXCEL_FILE_PATH_EXPORT_TEXT =  "resource/excel_file_{}.xlsx"
def standard_read_excel(file_path):
    """标准的读取excel操作"""
    df = pd.read_excel(file_path)
    print(df)

def standard_write_excel(file_path):
    data = [
        {"id": 1, "name": "张三", "email": "zhang@test.com", "age": 25, "department": "技术部"},
        {"id": 2, "name": "李四", "email": "li@test.com", "age": 30, "department": "销售部"},
        {"id": 3, "name": "王五", "email": "wang@test.com", "age": 35, "department": "技术部"},
    ]
    headers = {
        "id": "编号",
        "name": "姓名",
        "email": "邮箱",
        "age": "年龄",
        "department": "部门"
    }
    export(file_name=file_path, data=data,headers=headers)

def export(file_name:str,data,headers:dict=None):
    """headers 是一个字典，将数据字段名隐射到表头"""
    print("export ===================")

    df = pd.DataFrame(data)
    df = df.rename(columns=headers)

    # 导出到 Excel
    df.to_excel(file_name, index=False, sheet_name='员工数据')
    print("export end ===================")



def main():
    # standard_read_excel(EXCEL_FILE_PATH_TEXT)
    version = 3
    standard_write_excel(EXCEL_FILE_PATH_EXPORT_TEXT.format(version))


if __name__ == "__main__":
    main()
