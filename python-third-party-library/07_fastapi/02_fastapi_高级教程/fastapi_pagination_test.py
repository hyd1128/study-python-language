from fastapi import FastAPI
from fastapi_pagination import add_pagination, Page, paginate
from pydantic import BaseModel


class UserOut(BaseModel):
    name: str = "Steve"
    surname: str = "Rogers"


users_data = [
    {"name": "Steve1", "surname": "Rogers"},
    {"name": "Steve2", "surname": "Rogers"},
    {"name": "Steve3", "surname": "Rogers"},
    {"name": "Steve4", "surname": "Rogers"},
    {"name": "Steve5", "surname": "Rogers"},
    {"name": "Steve6", "surname": "Rogers"},
    {"name": "Steve7", "surname": "Rogers"},
    {"name": "Steve8", "surname": "Rogers"},
    # 可添加更多用户数据
]

app = FastAPI()

add_pagination(app)  # 添加分页到您的应用


@app.get("/users", response_model=Page[UserOut])
async def get_users():
    return paginate(users_data)



