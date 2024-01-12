from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel


class pessoa(BaseModel):
    name: str
    idade: Union[int, None] = None
    peso: float
    nacionalidade: Union[str, None] = None


API = FastAPI()

@API.post("/items")
async def pessoa(item: pessoa):
    return item