# Python Standard Lib
from typing import Optional, List

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI, Body, File, UploadFile


class PublishTableFile(BaseModel):
    file: UploadFile = File(..., description="A file read as UploadFile")
    channel: str
    dto_name: str
    column_filter: List[dict]
