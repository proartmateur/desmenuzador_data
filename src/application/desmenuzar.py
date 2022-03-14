from typing import List, Callable

from src.application.data_getter import get_columns, get_rows, add_idx_filters
from src.domain.dto_build import build_dto


def desmenuzar(
        raw_data,
        filters: List[dict],
        callback: Callable,
        channel: str
):
    r = raw_data
    cols = get_columns(r)
    print(cols)
    rows = get_rows(r)
    filters = add_idx_filters(filters, cols)

    for row in rows:
        dto = build_dto(row, filters)
        callback(dto, channel)
