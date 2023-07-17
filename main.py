from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}/")
async def read_items(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)],
        q: str Query()
):
    """
    le: less then or equal 
    lt: less than
    gt: greater than
    can also be applied, and not only in Path,
    but also in Query
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
