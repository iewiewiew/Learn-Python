# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/25 10:11
@description  FastAPI 例子
"""

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.models import Response
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str


app = FastAPI()


@app.get("/items/")
def read_items():
    """
    curl -X GET http://127.0.0.1:8000/items/
    """
    return [{"name": "aaaa"}, {"description": "bbbb"}]


@app.post("/items/")
def create_item(item: Item):
    """
    curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "description": "123"}' http://127.0.0.1:8000/items/
    """
    return {"message": "Item created"}


@app.put("/items/{item_id}")
def replace_item(item_id: str, item: Item):
    """
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "John", "description": "123"}' http://127.0.0.1:8000/items/123
    """
    return {"message": "Item replaced", "id": item_id}


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    """
    curl -X DELETE http://127.0.0.1:8000/items/123
    """
    return {"message": "Ttem deleted"}


@app.options("/items/")
def get_item_options():
    """
    curl -X OPTIONS http://127.0.0.1:8000/items/
    """
    return {"additions": ["aa", "bb"]}


@app.head("/items/", status_code=204)
def get_items_header(response: Response):
    """
    curl -X HEAD http://127.0.0.1:8000/items/ # 不知道咋测试
    """
    response.headers["X-Cat-Dog"] = "Alone in the world"


@app.patch("/items/")
def update_item(item: Item):
    """
    curl -X PATCH -H "Content-Type: application/json" -d '{"name": "John", "description": "123"}' http://127.0.0.1:8000/items/
    """
    return {"message": "Item updated is place"}


if __name__ == '__main__':
    uvicorn.run(app)
