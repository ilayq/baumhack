from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from multiprocessing import Process
import time

from Filter import FilterList
from get_csv import download_csv
from get_table_handler import get_table_handler
from save_to_db_handler import save_to_db_handler
from upload_from_db_handler import upload_from_db_handler


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/get_table', response_class=JSONResponse)
async def get_table(page: int, count: int,
                    sort: int = -1, search: str = None, reverse: bool = False,
                    filters: FilterList = None):
    return await get_table_handler(page, count, sort, reverse, search, filters)


@app.get('/save_table', response_class=FileResponse)
async def save_table_to_db():
    await save_to_db_handler()
    return FileResponse("db.db",
                        media_type="application/octet-stream",
                        filename="db.db")


@app.post('/upload_table', response_class=JSONResponse)
async def upload_from_db(db: UploadFile):
    await upload_from_db_handler(db)
    return {}


def update_func():
    while 1:
        print("updating")
        download_csv()
        time.sleep(600)


if __name__ == '__main__':
    update_thread = Process(target=update_func)
    update_thread.start()
    uvicorn.run("main:app", reload=True)
    update_thread.terminate()
