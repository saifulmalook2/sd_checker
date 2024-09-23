
import logging
from fastapi import FastAPI, Depends, Form, Body, Query
from typing import List
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder 
import os        
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
from utils import check_company, check_date


app = FastAPI()


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

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