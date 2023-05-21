import os.path
import csv
from settings import CSV_DELIMITER


from db.models import CityORM
from db.engine import engine, Base
from sqlalchemy import select


async def write_to_csv():
    query = select(CityORM)
    with engine.connect() as db, open('data.csv', 'w', newline='') as file:
        for row in db.execute(query).all():
            writer = csv.writer(file, delimiter=CSV_DELIMITER)
            r = list(row)
            r[0] = str(r[0])
            writer.writerow(r[0])


async def upload_from_db_handler(file):
    with open("downloaded_db.db", "ab") as db:
        db.writelines(file.file.readlines())
    await write_to_csv()
