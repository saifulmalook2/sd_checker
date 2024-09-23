
import logging
from fastapi import FastAPI, Depends, Form, Body, Query
from typing import List
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder 
import os        
from utils import check_company, check_date

logging.basicConfig(format="%(levelname)s     %(message)s", level=logging.INFO)
# hack to get rid of langchain logs
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)


def file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.isfile(file_path)



app = FastAPI()



@app.get("/")
async def root():
    return {"msg": "OK"}



@app.post("/name_check")
async def name_check( html_text: str = Body(..., media_type="text/html"), company_name: str = Query(...)):
    response = await check_company(html_text, company_name)
    return  response

    
@app.post("/date_check")
async def name_check( html_text: str = Body(..., media_type="text/html"), given_date: str = Query(...)):
    response = await check_date(html_text, given_date)
    return  response
    

    data_doc = jsonable_encoder(data)
    name = data_doc['file_name']

    file_name = f"{evidence_id}_{name}"
    if file_exists('docs', file_name):
        print(f"{name} exists.")
        response = await extract_mistakes_from_pdf(file_name)
        return {"pages" : response}
    else:
        return "File does not exist"