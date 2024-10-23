
import logging
from fastapi import FastAPI, Depends, Form, Body, Query, HTTPException, Request,  UploadFile, File, Depends
from typing import List
from pydantic import BaseModel
import shutil
from fastapi.encoders import jsonable_encoder 
import os        
from fastapi.middleware.cors import CORSMiddleware  
from utils import check_company, check_date, check_grammar, check_sections, check_infrastructure
from desc_helpers import process_file, verify_control
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

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  )

async def verify_request(request: Request):
    headers = request.headers
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
async def name_check( company_name: str, sections: dict = Body(...)):
    sections.pop("company_name", None)

    company_name = normalize_company_name(company_name)

    logging.info(f"Checking Name {company_name}")

    response = await check_company(sections, company_name)
    logging.info(response)
    return  response


    
@app.post("/date_check/")
async def date_check(start_date: str = Query(...), end_date: str = Query(...), sections: dict = Body(...), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Date {start_date} {end_date}")
    sections.pop("company_name", None)

    response = await check_date(sections, start_date, end_date)
    return  response

@app.post("/grammar_check/{company_name}")
async def grammar_check( company_name: str, sections: dict = Body(...), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Grammer")
    sections.pop("company_name", None)

    response = await check_grammar(sections, company_name)
    return  response

@app.post("/section_check")
async def section_check( sections: dict = Body(...), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Sections")
    sections.pop("company_name", None)
    
    response = await check_sections(sections)
    return  response

@app.post("/service_check/{service_name}")
async def service_check( service_name: str, sections: dict = Body(...), headers: dict = Depends(verify_request)):
    logging.info(f"Checking Provider {service_name}")
    sections.pop("company_name", None)
    

    response = await check_infrastructure(sections, service_name)
    logging.info(response)
    return  response




@app.post("/get_desc/{client_id}")
async def get_desc(
    client_id: str,
    evidence_files: List[UploadFile] = File(...),
    policy_files: List[UploadFile] = File(...),
    name: str = Form(...),
    description: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...)

):
    saved_files = []

    # Process and download evidence files
    for evidence_file in evidence_files:
        filename_with_client_id = f"{client_id}_evidence_{evidence_file.filename}"
        file_path = os.path.join("docs", filename_with_client_id)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(evidence_file.file, buffer)
        saved_files.append(filename_with_client_id)

    # Process and download policy files
    for policy_file in policy_files:
        filename_with_client_id = f"{client_id}_policy_{policy_file.filename}"
        file_path = os.path.join("docs", filename_with_client_id)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(policy_file.file, buffer)
        saved_files.append(filename_with_client_id)

    contents = await process_file(saved_files)

    ai_response = await verify_control(contents, description, start_date, end_date)

    return ai_response