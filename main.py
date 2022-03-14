# Python Standard Lib
from typing import Optional, List

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI, Body, File, UploadFile

app = FastAPI()


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


# Basic Path CSV
# 1 - Upload file and get list of columns
# 2 - Send columns filters, file & channel to make dtos, save dto in db & start to publish row(dto) by row
# 3 - Subscribe other apps to channel and listen the data stream

@app.post('/columns_csv/')
def retrieve_csv_col_names(
        file: UploadFile = File(..., description="A file read as UploadFile")
):
    """Retrieve column names as a list of strings"""
    return {"filename": file.filename}


class PublishTableFile(BaseModel):
    file: UploadFile = File(..., description="A file read as UploadFile")
    channel: str
    dto_name: str
    column_filter: List[dict]


@app.post('/publish_csv/')
def publish_csv(publish_file: PublishTableFile = Body(...)):
    """Process CSV, filter columns & publish dto for each row in file"""
    return {"filename": publish_file.file}
