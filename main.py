# Python Standard Lib
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI, Body

from app.http.routers import csv

app = FastAPI()
app.include_router(csv.router)


# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get('/')
def home():
    return {"hello": "worldd"}


@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person
