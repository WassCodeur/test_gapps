from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Hello I'm about to start learning fastapi"}

@app.post("/items/")
def add(items: Item):
    return items
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{name}")
def getname(name: int):
    return {"message": f"hello you're {name}"}