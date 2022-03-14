# FastApi
from fastapi import FastAPI

# App
from app.http.routers import csv

app = FastAPI()
app.include_router(csv.router)


@app.get('/')
def home():
    return {"hello": "worldd"}
