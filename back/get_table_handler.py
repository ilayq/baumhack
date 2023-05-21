from typing import List

import pydantic

from Filter import FilterList
from get_csv import get_rows_from_csv


class Response(pydantic.BaseModel):
    rows: int
    data: List[List[str]]


async def get_table_handler(page: int, count: int,
                            sort: int = -1, reverse: bool = False, search: str = None,
                            filters: FilterList = None) -> Response:
    all_rows = list(get_rows_from_csv())
    if sort > -1:
        try:
            all_rows.sort(key=lambda element: int(element[sort]), reverse=reverse)
        except ValueError:
            all_rows.sort(key=lambda element: element[sort], reverse=reverse)
    if search:
        all_rows = list(filter(lambda element: search in element, all_rows))
    if filters:
        for filt in filters.filters:
            if filt.filter_ == 'l':
                all_rows = list(filter(lambda element: element[filt.column] < filt.value, all_rows))
            elif filt.filter_ == 'le':
                all_rows = list(filter(lambda element: element[filt.column] <= filt.value, all_rows))
            elif filt.filter_ == 'e':
                all_rows = list(filter(lambda element: element[filt.column] == filt.value, all_rows))
            elif filt.filter_ == 'eg':
                all_rows = list(filter(lambda element: element[filt.column] >= filt.value, all_rows))
            elif filt.filter_ == 'g':
                all_rows = list(filter(lambda element: element[filt.column] > filt.value, all_rows))
    response = []
    for idx in range((page - 1) * count, min(len(all_rows), page*count)):
        response.append(all_rows[idx])
    return Response(rows=len(all_rows), data=response)
