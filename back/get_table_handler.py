from typing import List
from Filter import FilterList
from get_csv import get_rows_from_csv

# todo filters
# async def get_table_handler(page: int, count: int,
#                             sort: int = -1, reverse: bool = False, search: str = None,
#                             filters: FilterList = None) -> List[List[str]]:
#     iterator = get_rows_from_csv()
#     response = []
#     if filters:
#         temp_response = list(get_rows_from_csv())
#         for filt in filters.filters:
#             if filt.filter_ == 'l':
#                 temp_response = list(filter(lambda element: element[filt.column] < filt.value, temp_response))
#             elif filt.filter_ == 'le':
#                 temp_response = list(filter(lambda element: element[filt.column] <= filt.value, temp_response))
#             elif filt.filter_ == 'e':
#                 temp_response = list(filter(lambda element: element[filt.column] == filt.value, temp_response))
#             elif filt.filter_ == 'eg':
#                 temp_response = list(filter(lambda element: element[filt.column] >= filt.value, temp_response))
#             elif filt.filter_ == 'g':
#                 temp_response = list(filter(lambda element: element[filt.column] > filt.value, temp_response))
#         if search:
#             temp_response = list(filter(lambda element: search in element, temp_response))
#         for i in range()
#
#     else:
#         if not search:
#             try:
#                 for _ in range((page - 1) * count):
#                     next(iterator)
#                 for _ in range(count):
#                     response.append(next(iterator))
#             except StopIteration:
#                 return response
#         else:
#             yielded = 0
#             while yielded < page * count:
#                 try:
#                     row = next(iterator)
#                     for col in row:
#                         if search in col:
#                             if yielded >= (page - 1) * count:
#                                 response.append(row)
#                             yielded += 1
#                             break
#                 except StopIteration:
#                     break
#     if sort > -1:
#         response.sort(key=lambda column: column[sort], reverse=reverse)
#     return response

async def get_table_handler(page: int, count: int,
                            sort: int = -1, reverse: bool = False, search: str = None,
                            filters: FilterList = None) -> List[List[str]]:
    all_rows = list(get_rows_from_csv())
    if sort > -1:
        all_rows.sort(key=lambda element: element[sort], reverse=reverse)
    if search:
        pop_c = 0
        f = False
        for i in range(len(all_rows)):
            for j in range(len(all_rows[i])):
                if search in all_rows[i][j]:
                    f = True
                    break
            if not f:
                all_rows.pop(i-pop_c)
                pop_c += 1
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
    return response
