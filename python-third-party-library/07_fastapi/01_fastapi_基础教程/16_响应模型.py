#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/16 10:57
# @Author : limber
# @desc :


from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
