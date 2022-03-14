# Python Standard Lib
from typing import Optional, List

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI, Body, File, UploadFile

from fastapi import APIRouter

from app.http.models.publish_table_file import PublishTableFile

router = APIRouter(
    prefix="/csv",
    tags=["csv"],
    # dependencies=[Depends(csv_router)],
    responses={404: {"description": "Not found"}},
)


# Basic Path CSV
# 1 - Upload file and get list of columns
# 2 - Send columns filters, file & channel to make dtos, save dto in db & start to publish row(dto) by row
# 3 - Subscribe other apps to channel and listen the data stream

@router.post('/columns/')
def retrieve_csv_col_names(
        file: UploadFile = File(..., description="A file read as UploadFile")
):
    """Retrieve column names as a list of strings"""
    return {"filename": file.filename}


@router.post('/publish/')
def publish_csv(publish_file: PublishTableFile = Body(...)):
    """Process CSV, filter columns & publish dto for each row in file"""
    return {"filename": publish_file.file}
