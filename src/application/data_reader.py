import os
from typing import List

from src.shared.file_read import traverse


def read_csv_fake() -> List[list]:
    header = ['uno', 'dos', 'Tres', '4tro']

    row1 = [
        'hola',
        'mundo',
        301,
        4.5
    ]
    res = [
        header,
        row1,
        row1
    ]
    for row in res:
        yield row


def read_csv(file: str) -> List[list]:
    if not os.path.exists(file):
        raise Exception("No existe el csv")

    # with open(file, "r", encoding="utf-8") as fil:
    #     data = fil.readlines()
    #     for line in data:
    #         yield line.split(',')
    return traverse(file)
