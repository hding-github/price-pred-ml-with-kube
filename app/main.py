from typing import Union
from fastapi import FastAPI
from fastapi import APIRouter, Request, Response
import pandas as pd
import ml_functions
import uvicorn


ml_functions.test()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/models/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/prediction/{item_id}")
def read_item(item_id: int, data: Union[str, None] = None, model: Union[str, None] = None):
    strResults = ml_functions.prediction(data, model)
    return {"item_id": item_id, "q": strResults}


if __name__ == "__main__":
    print("****")