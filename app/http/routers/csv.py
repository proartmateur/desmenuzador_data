# FastApi
import json
import os

from fastapi import Body, File, UploadFile

from fastapi import APIRouter

from app.http.models.publish_table_file import PublishTableFile
from src.application.data_getter import get_columns
from src.application.data_reader import read_csv

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
async def retrieve_csv_col_names(
        file: UploadFile = File(..., description="A file read as UploadFile")
):
    """Retrieve column names as a list of strings"""
    content = await file.read()
    cont = content.decode("utf-8")

    print(cont)
    tmp_name = 'tmp_csv.csv'
    base_path = "/Users/ennima/Devs/diana/demenuzador"
    file = os.path.join(base_path, tmp_name)
    with open(file, 'w', encoding='utf-8') as fil:
        fil.write(cont)
    del content
    del cont

    r = read_csv(file)
    cols = get_columns(r)

    return {
        "cols": cols
    }


@router.post('/publish/')
def publish_csv(publish_file: PublishTableFile = Body(...)):
    """Process CSV, filter columns & publish dto for each row in file"""
    return {"filename": publish_file.file}
