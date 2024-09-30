
import logging
from fastapi import FastAPI, Depends, Form, Body, Query, HTTPException, Request
from typing import List
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder 
import os        
from fastapi.middleware.cors import CORSMiddleware  
from utils import check_company, check_date, check_grammar, check_sections, check_infrastructure
import re
from cryptography.fernet import Fernet


logging.basicConfig(format="%(levelname)s     %(message)s", level=logging.INFO)
# hack to get rid of langchain logs
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)

app = FastAPI()

key = os.getenv("SECRET_KEY")
KEY = key.encode()
cipher_suite = Fernet(KEY)

logging.info(f"key {key}")
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  )

async def verify_request(request: Request):
    headers = request.headers
    logging.info(f"headers {headers}")
    auth_token = headers.get('Authorization') 
    
    if auth_token:
        try:
            token = auth_token.split(' ')[1]            
            decrypted_token = cipher_suite.decrypt(token.encode()).decode()
            
            # Compare decrypted token with expected value
            if decrypted_token != os.getenv("SECRET_TOKEN"):
                logging.info("Invalid Token")

                raise HTTPException(status_code=403, detail="Invalid token")
            else:
                logging.info("Valid Token")
                return
        except Exception as e:
            logging.error(f"Token decryption error: {e}")
            raise HTTPException(status_code=403, detail="Invalid token")
    else:
        raise HTTPException(status_code=400, detail="Authorization token missing")
    
@app.get("/")
async def root():
    return {"msg": "OK"}


def normalize_company_name(name):
    return re.sub(r'[^a-zA-Z0-9\s]', '', name)

@app.post("/name_check/{company_name}")
async def name_check( company_name: str, html_text: str = Body(..., media_type="text/html"), headers: dict = Depends(verify_request)):
    company_name = normalize_company_name(company_name)

    logging.info(f"Checking Name {company_name}")

    response = await check_company(html_text, company_name)
    logging.info(response)
    return  response

    
@app.post("/date_check/")
async def date_check(start_date: str = Query(...), end_date: str = Query(...), html_text: str = Body(..., media_type="text/html"), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Date {start_date} {end_date}")
    response = await check_date(html_text, start_date, end_date)
    return  response

@app.post("/grammar_check")
async def grammar_check( html_text: str = Body(..., media_type="text/html"), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Grammer")
    response = await check_grammar(html_text)
    return  response

@app.post("/section_check")
async def section_check( html_text: str = Body(..., media_type="text/html"), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Sections")
    response = await check_sections(html_text)
    return  response

@app.post("/service_check/{service_name}")
async def service_check( service_name: str, html_text: str = Body(..., media_type="text/html"), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Provider {service_name}")
    response = await check_infrastructure(html_text, service_name)
    logging.info(response)
    return  response
