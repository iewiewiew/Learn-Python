# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/2/18 11:18
@description  FastAPI 例子
参考资料：https://wangchujiang.com/reference/docs/fastapi.html
pip install python-multipart
"""

from fastapi import FastAPI, Path, Query, Cookie, Header, Form, UploadFile
from fastapi.responses import HTMLResponse
from typing import Union, List
from pydantic import BaseModel
from typing_extensions import Annotated
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    """
    curl http://127.0.0.1:8000
    """
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id):
    """
    最基本的路径参数
    curl http://127.0.0.1:8000/items/123
    """
    return {"item_id": item_id}


@app.get("/items/{item_id}/{user_id}")
def read_item2(item_id, user_id):
    """
    多个路径参数
    curl http://127.0.0.1:8000/items/123/456
    """
    return {"item_id": item_id, "user_id": user_id}


@app.get("/items3/{item_id}")
def read_item3(item_id: int):
    """
    有类型的路径参数
    curl http://127.0.0.1:8000/items3/123
    """
    return {"item_id": item_id}


@app.get("/file/{file_path:path}")
def read_item4(file_path):
    """
    文件路径参数
    curl http://127.0.0.1:8000/file//tmp.txt
    """
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items5/")
def read_item5(skip: int = 0, limit: int = 10):
    """
    带默认值的查询参数 注：浏览器访问正常，curl 访问报错
    http://127.0.0.1:8000/items5/?skip=0&limit=2
    """
    return fake_items_db[skip: skip + limit]


@app.get("/items6/{item_id}")
def read_item6(item_id: str, q: Union[str, None] = None):
    """
    可选查询参数
    http://127.0.0.1:8000/items6/123?q=admin
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/user/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    """
    多路径多查询参数
    http://127.0.0.1:8000/user/1/items/2
    http://127.0.0.1:8000/user/1/items/2?q=query&short=true
    """
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a log description"})
    return item


@app.get("/items7/{item_id}")
def read_user_item2(item_id: str, needy: str):
    """
    必需查询参数
    http://127.0.0.1:8000/items7/123?needy=yes
    """
    item = {"item_id": item_id, "needy": needy}
    return item


class Item(BaseModel):
    name: str = '小明'
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post("/items/")
def create_item(item: Item):
    """
    curl -X 'POST' \
      'http://127.0.0.1:8000/items/' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "name": "小明",
      "description": "string",
      "price": 0,
      "tax": 0
    }'
    """
    print(item.name)
    return item


def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/read_items2")
def read_items2(q: Union[List[str], None] = Query(default=None)):
    """
    多个相同的查询参数
    http://127.0.0.1:8000/read_items2/?q=foo&q=bar
    """
    query_items = {"q": q}
    return query_items


@app.get("/read_items3/{item_id}")
def read_items3(item_id: Annotated[int, Path(title="The ID of the item to get")],
                q: Annotated[Union[str, None], Query(alias="item-query")] = None, ):
    """
    声明元数据
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
def read_items3(ads_id: Annotated[Union[str, None], Cookie()] = None):
    """
    Cookie 参数
    """
    return {"ads_id": ads_id}


@app.get("/items")
def read_items4(user_agent: Annotated[Union[str, None], Header()] = None,
                item_id: Annotated[Union[int, None], Header(ge=1)] = None):
    """
    Header 参数
    """
    return {"User-Agent": user_agent, "items_id": item_id}


@app.post("/login/")
def login(username: str = Form(), password: str = Form()):
    return {"username": username}


@app.post("uploadfile")
def create_upload_file(file: UploadFile):
    print(file.file.read().decode())
    return {"filenames": file.filename, "type": str(type(file.file))}


@app.get("/")
def main():
    content = """
    <form action="/uploadfile/" enctype="multipart/form-data" method="post">
    <input name="file" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)


if __name__ == '__main__':
    uvicorn.run(app)
