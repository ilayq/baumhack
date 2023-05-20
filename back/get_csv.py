import os.path

import wget

from settings import FILEPATH, CSV_DELIMITER, FILEURL
import csv


def download_csv() -> None:
    try:
        if os.path.exists('data.csv'):
            os.remove('data.csv')
        wget.download(FILEURL, "data.csv")
    except Exception:
        pass


def get_rows_from_csv():
    with open(FILEPATH) as file:
        reader = csv.reader(file, delimiter=CSV_DELIMITER)
        for row in reader:
            yield row


if __name__ == '__main__':
    download_csv()
