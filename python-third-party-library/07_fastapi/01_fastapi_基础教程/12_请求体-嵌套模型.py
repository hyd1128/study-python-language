#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/16 9:46
# @Author : limber
# @desc :

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Union, List

app = FastAPI()

# 将子模型用作类型
# class Image(BaseModel):
#     url: str
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     image: Image | None = None


# 特殊类型和校验
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     image: Image | None = None


# 带有一组子模型的属性
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     images: list[Image] | None = None


# 深度嵌套模型
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
