
import logging
from fastapi import FastAPI, Depends, Form, Body, Query
from typing import List
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder 
import os        
from fastapi.middleware.cors import CORSMiddleware  
from utils import check_company, check_date, check_grammar, check_sections, check_infrastructure
import re

logging.basicConfig(format="%(levelname)s     %(message)s", level=logging.INFO)
# hack to get rid of langchain logs
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)

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


def normalize_company_name(name):
    return re.sub(r'[^a-zA-Z0-9\s]', '', name)

@app.post("/name_check/{company_name}")
async def name_check( company_name: str, html_text: str = Body(..., media_type="text/html")):
    company_name = normalize_company_name(company_name)

    logging.info(f"Checking Name {company_name}")

    response = await check_company(html_text, company_name)
    logging.info(response)
    return  response

    
@app.post("/date_check/")
async def date_check(start_date: str = Query(...), end_date: str = Query(...), html_text: str = Body(..., media_type="text/html")):
    logging.info(f"Checking Date {start_date} {end_date}")
    response = await check_date(html_text, start_date, end_date)
    return  response

@app.post("/grammar_check")
async def grammar_check( html_text: str = Body(..., media_type="text/html")):
    logging.info(f"Checking Grammer")
    response = await check_grammar(html_text)
    return  response

@app.post("/section_check")
async def section_check( html_text: str = Body(..., media_type="text/html")):
    logging.info(f"Checking Sections")
    response = await check_sections(html_text)
    return  response

@app.post("/service_check")
async def service_check( html_text: str = Body(..., media_type="text/html")):
    logging.info(f"Checking Provider")
    response = await check_infrastructure(html_text)
    logging.info(response)
    return  response
