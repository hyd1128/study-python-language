#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 16:02
# @Author : limber
# @desc :


from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    # 必选参数
    name: str
    # 包含默认值 可选参数
    description: str | None = None
    # 必选参数
    price: float
    # 可选参数
    tax: float | None = None


app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     # 自动序列化为json
#     return item

# 请求体+路径参数
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


# 请求体+路径参数+查询参数
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    """
        函数参数按如下规则进行识别：

        **路径**中声明了相同参数的参数，是路径参数
        类型是（int、float、str、bool 等）**单类型**的参数，是**查询**参数
        类型是 Pydantic 模型**的参数，是**请求体
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# 请求体
# @app.post("/items/")
# async def create_item(item: Item):
#     print(type(item))
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
