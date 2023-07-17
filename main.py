from typing import Annotated


from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, HttpUrl


app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
