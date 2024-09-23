
import logging
from fastapi import FastAPI, Depends, Form, Body, Query
from typing import List
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder 
import os        
from fastapi.middleware.cors import CORSMiddleware  
from utils import check_company, check_date


app = FastAPI()


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  )

@app.get("/")
async def root():
    return {"msg": "OK"}



@app.post("/name_check/{company_name}")
async def name_check( company_name: str, html_text: str = Body(..., media_type="text/html")):
    logging.info(f"Checking Name {company_name}")
    response = await check_company(html_text, company_name)
    logging.info(response)
    return  response

    
@app.post("/date_check/{given_date}")
async def name_check(given_date: str, html_text: str = Body(..., media_type="text/html")):
    response = await check_date(html_text, given_date)
    return  response
