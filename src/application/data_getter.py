from typing import List, Iterable


def clean_row(row: list) -> list:
    res = []

    for c in row:
        res.append(c.strip())

    return res


def get_columns(data: Iterable) -> List[str]:
    count = 0
    res = []
    for row in data:
        if count == 0:
            return clean_row(row)


def get_rows(data: Iterable):
    count = 0
    for row in data:
        count += 1
        if count > 0:
            yield clean_row(row)


def get_row_idx(row: str, header: List[str]):
    i = 0
    for c in header:
        if c == row:
            return i
        i += 1


def add_idx_filters(filters: List[dict], header) -> List[dict]:
    r = []
    for f in filters:
        i = get_row_idx(f['col'], header)
        f["id"] = i
        r.append(f)
    return r
