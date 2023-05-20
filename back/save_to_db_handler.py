from sqlalchemy.orm import Session

import os
import datetime

from get_csv import get_rows_from_csv
from db.engine import engine
from db.models import CityORM, Base


async def save_to_db_handler():
    if os.path.exists("db.db"):
        os.remove("db.db")
    if os.path.exists("db.db-journal"):
        os.remove("db.db-journal")

    Base.metadata.create_all(engine)

    with Session(engine) as db:
        c = 0
        for row in get_rows_from_csv():
            print(row, c)
            c += 1
            db.add(CityORM(
                date=datetime.date.fromisoformat(row[0]),
                city_name=row[1],
                state=row[2],
                all_covid_accidents=row[3],
                new_accidents=row[4],
                lethal_accidents=row[5]
            ))
        db.commit()
        db.close()
