from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import uvicorn

from handlers import get_table_handler


app = FastAPI()


@app.get('/get_table', response_class=JSONResponse)
async def get_table(page: int, count: int, filter_: str = None, sort=False):
    return await get_table_handler(page, count, filter_, sort)


@app.post('/save_table', response_class=FileResponse)
async def save_table_to_db(table: str):
    ...


@app.post('/upload_table')
async def upload_from_db(db: UploadFile):
    ...


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
