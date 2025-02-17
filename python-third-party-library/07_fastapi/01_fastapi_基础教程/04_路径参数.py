#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 14:04
# @Author : limber
# @desc :


from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

# fastapi支持使用python字符串格式化语法声明路径参数
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# 声明路径参数的类型
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # 比较枚举元素
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": # 获取枚举值
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
