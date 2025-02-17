#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/15 17:25
# @Author : limber
# @desc :


from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


"""
Field: 定义模型上的字段
    default: 默认值
    gt: 大于
    le: 小于等于
    
Literal: Literal 可以用来向类型检查器说明被注解的对象具有与所提供的字面量之一相同的值。
type Mode = Literal['r', 'rb', 'w', 'wb'] 表示Mode具有列表中的任意一个值
"""
class FilterParams(BaseModel):
    # 禁止额外的查询参数
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


# 使用pydantic模型查询参数
@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query



