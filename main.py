from typing import Annotated

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


@app.put("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(
            title="The ID of the item to get", ge=0, le=1000)],
        q: str,
        item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
