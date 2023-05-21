import os.path

import wget

from settings import FILEPATH, CSV_DELIMITER, FILEURL
import csv


def download_csv() -> None:
    try:
        if os.path.exists('data.csv'):
            wget.download(FILEURL, out="data1.csv")
            os.remove('data.csv')
            os.rename("data1.csv", 'data.csv')
        else:
            wget.download(FILEURL, out="data.csv")
    except Exception:
        pass


def get_rows_from_csv():
    with open(FILEPATH) as file:
        reader = csv.reader(file, delimiter=CSV_DELIMITER)
        for row in reader:
            yield row
        file.close()


if __name__ == '__main__':
    download_csv()
