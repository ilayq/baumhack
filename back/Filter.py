from pydantic import BaseModel
from typing import List, Union


class Filter(BaseModel):
    column: int
    filter_: str
    value: Union[str, int]


class FilterList(BaseModel):
    filters: List[Filter]
