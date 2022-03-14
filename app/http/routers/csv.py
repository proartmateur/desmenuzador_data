# FastApi
import json
import os

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable

from fastapi import Body, File, UploadFile

from fastapi import APIRouter

from app.http.controllers.get_columns_from_csv import get_columns_from_csv
from app.http.models.publish_table_file import PublishTableFile
from src.application.data_getter import get_columns, get_head_rows
from src.application.data_reader import read_csv

router = APIRouter(
    prefix="/csv",
    tags=["csv"],
    # dependencies=[Depends(csv_router)],
    responses={404: {"description": "Not found"}},
)


def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path


def handle_upload_file(
        upload_file: UploadFile, handler: Callable[[Path], None]
) -> None:
    tmp_path = save_upload_file_tmp(upload_file)
    try:
        handler(tmp_path)  # Do something with the saved temp file
    finally:
        tmp_path.unlink()  # Delete the temp file


# Basic Path CSV
# 1 - Upload file and get list of columns
# 2 - Send columns filters, file & channel to make dtos, save dto in db & start to publish row(dto) by row
# 3 - Subscribe other apps to channel and listen the data stream

@router.post('/columns/')
async def retrieve_csv_col_names(
        file: UploadFile = File(..., description="A file read as UploadFile")
):
    """Retrieve column names as a list of strings"""
    # content = await file.read()
    # cont = content.decode("utf-8")
    #
    # print(cont)
    # tmp_name = 'tmp_csv.csv'
    # base_path = "/Users/ennima/Devs/diana/demenuzador"
    # file_a = os.path.join(base_path, tmp_name)
    # with open(file_a, 'w', encoding='utf-8') as fil:
    #     fil.write(cont)
    # del content
    # del cont

    tmp_path = save_upload_file_tmp(file)

    r = read_csv(tmp_path)
    cols = get_columns(r)
    head_rows = get_head_rows(r)

    tmp_path.unlink()

    return {
        "cols": cols,
        "head_rows": head_rows,
        "tmp": tmp_path
    }


@router.post('/publish/')
def publish_csv(publish_file: PublishTableFile = Body(...)):
    """Process CSV, filter columns & publish dto for each row in file"""
    return {"filename": publish_file.file}
