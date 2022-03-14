import os

from fastapi import UploadFile, File

from src.application.data_getter import get_columns
from src.application.data_reader import read_csv


async def get_columns_from_csv(
        file
):
    r = read_csv(file)
    cols = get_columns(r)

    return {
        "cols": cols
    }
