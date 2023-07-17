from typing import Annotated

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}/")
async def update_item(
        item_id: int, item: Item, user: User
):
    results = {"item_id": item_id, "item": item, "user": user}
    return results
