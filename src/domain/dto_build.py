from typing import List


def build_dto(row: list, filter_cols: List[dict]):
    dto = {}
    for item in filter_cols:
        id = item["id"]
        name = item["name"]
        dto[name] = row[id]

    return dto
