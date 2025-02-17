#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/17 16:49
# @Author : limber
# @desc :

from fastapi import FastAPI, HTTPException, Depends, Header, Request
from typing import Dict, Annotated

from starlette import status

app = FastAPI()


async def get_current_user(request: Request) -> Dict:
    body = await request.json()
    if body.get("token") != "abcdef":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invaild or mssing token"
        )
    return {"username": "admin"}


@app.post("/protect/")
async def protect_route(user: Dict = Depends(get_current_user)):
    return {
        "message": f"Hello , {user['username']}"
    }
