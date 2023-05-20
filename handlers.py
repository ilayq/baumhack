from typing import List

from get_csv import get_rows_from_csv


async def get_table_handler(page: int, count: int, filter_: str = None, sort: bool = False) -> List[List[str]]:
    iterator = get_rows_from_csv()
    response = []
    if not filter_:
        try:
            for _ in range((page - 1) * count):
                next(iterator)
            for _ in range(count):
                response.append(next(iterator))
        except StopIteration:
            return response
    else:
        yielded = 0
        while yielded < page * count:
            try:
                row = next(iterator)
                for col in row:
                    print(col)
                    if filter_ in col:
                        if yielded >= (page - 1) * count:
                            response.append(row)
                        yielded += 1
                        break
            except StopIteration:
                break
    if sort:
        response.sort()
    return response
