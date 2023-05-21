import os.path
import csv
from settings import CSV_DELIMITER

from sqlalchemy import create_engine
from db.models import CityORM
from sqlalchemy import select


async def write_to_csv():
    query = select(CityORM)
    engine = create_engine("sqlite:///downloaded_db.db")
    with engine.connect() as db, open('data.csv', 'w', newline='') as file:
        for row in db.execute(query).all():
            print(row)
            writer = csv.writer(file, delimiter=CSV_DELIMITER)
            # r = list(row)
            # r[0] = str(r[0])
            writer.writerow(row)


async def upload_from_db_handler(file):
    with open("downloaded_db.db", "ab") as db:
        db.writelines(file.file.readlines())
    await write_to_csv()
