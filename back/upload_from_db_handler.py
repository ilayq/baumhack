import os.path
import csv
from settings import CSV_DELIMITER


from db.models import CityORM
from db.engine import engine
from sqlalchemy import select


async def write_to_csv():
    query = select(CityORM)
    with engine.connect() as db, open('data.csv', 'w', newline='') as file:
        for row in db.execute(query).all():
            writer = csv.writer(file, delimiter=CSV_DELIMITER)
            r = list(row)
            r[0] = str(r[0])
            writer.writerow(row)


async def upload_from_db_handler(file):
    if os.path.exists("db.db"):
        os.remove("db.db")
    with open("db.db", "ab") as db:
        db.writelines(file.file.readlines())
    await write_to_csv()


# TODO FILTERS, SORTS