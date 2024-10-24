from openai import AsyncAzureOpenAI
import os
import json
from bs4 import BeautifulSoup
import re
import tiktoken
import logging


os.environ["AZURE_OPENAI_API_VERSION"]="2024-02-15-preview"
os.environ["AZURE_OPENAI_DEPLOYMENT"]="prescientassurance"
os.environ["AZURE_OPENAI_API_KEY"]="e60e6f67ae3a444a90ed6e0341d8258a"
os.environ["AZURE_OPENAI_ENDPOINT"]="https://prescientassurance.openai.azure.com/"

logging.basicConfig(format="%(levelname)s     %(message)s", level=logging.INFO)
# hack to get rid of langchain logs
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)

client = AsyncAzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

def extract(soup):
    return '\n'.join([element.strip().replace('\u25cf', ' ') for element in soup.stripped_strings])


encoding = tiktoken.encoding_for_model("gpt-4o")

def get_chunks(text):
    """Efficiently get the number of tokens for a given text."""
    tokens = encoding.encode(text)
    
    print("Number of Tokens:",  len(tokens))
    max_tokens = 20000
    if len(tokens) < max_tokens:
        print("not split")
        return [text]
    else:
        print("split")

        chunks = []
        while len(text) > max_tokens:
            chunk = text[:max_tokens]
            last_period = chunk.rfind(".")
            if last_period != -1:
                chunk = chunk[:last_period + 1]  # Cut at last sentence end
            chunks.append(chunk)
            text = text[len(chunk):]
        chunks.append(text)  # Add the remaining text
        return chunks

async def check_company(sections, company_name):
    custom_response = {}
    for section, value in sections.items():
        logging.info(f"section {section}")
        if value:
            section_soup =  BeautifulSoup(value, 'html.parser')
            try:
                html_text = extract(section_soup)
                response = await client.chat.completions.create(
                            response_format={"type": "json_object"},
                            model="gpt-4o",
                            temperature = 0.5,
                            messages=[
                            {"role": "system", "content": "You are an assistant that matches text and strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
                            {
                                    "role": "user",
                                    "content": (
                                        f"Check the following report content for the name of the Company for which the report content is created. This report is created by the Prescient Security/Assurance Company (Cacilian) for the following company : {company_name}"
                                        f"Ensure the name mentioned in the content is the same as {company_name}, the correct company name is {company_name} for which the report was created."
                                        f"Return a list of incorrect names and misspelled names. Ignore the company 'Prescient Assurance LLC', 'Cacilian LLC', 'Security, 'Prescient Security' "
                                        f'''if the company name does not match, return a list of JSON objects, each containing the incorrect company name and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as 'mistakes: [{{"incorrect_company_name": "...", "sentence": "..."}}]'. The sentence should be 10-15 words at maximum. Find all the incorrect names and append the JSON to the list. content : {html_text}'''
                                    )
                                }            
                                ],
                        )
                response_text = response.choices[0].message.content.strip()
                filtered_response = json.loads(response_text)

                custom_response[section] = filtered_response
                logging.info(f"response {custom_response}")


            except Exception as e:
                print("Error", e)
                return custom_response
        else:
            custom_response[section] = []
             
            
    return custom_response
        
        

async def check_date(sections, start_date, end_date):
    custom_response = {}
    for section, value in sections.items():
        logging.info(f"section {section}")
        if value:
            section_soup =  BeautifulSoup(value, 'html.parser')
            try:
                html_text = extract(section_soup)
                response = await client.chat.completions.create(
                    response_format={"type": "json_object"},
                    model="gpt-4o",
                    temperature = 0.2,
                    messages=[
                        {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
                        {"role": "user", "content": f'''Check if the start date and end date mentioned in the following page content match the given 
                        start date = {start_date} and end date = {end_date}, the Date Format may be different. If there is a specific actual start date or end date mentioned in the content 
                        and it does not match the given dates, return a list of JSON objects. Each object should contain the incorrect date. If a specific date is not mentioned like the following : 2024-08-11, 11-08-24, 11-08-2024, 08-11-2024, 11 August 2024, it should not be flagged. 
                        Format the response as 'mistakes: [{{"incorrect_start_date": "...", "incorrect_end_date": "..."}}]'. 
                        If no dates are mentioned in the content then return an empty list.
                        Find all the incorrect dates and append each JSON object to the list. Page content: {html_text}'''}
                    ],
                )
                response_text = response.choices[0].message.content.strip()
                filtered_response = json.loads(response_text)
                custom_response[section] = filtered_response
                logging.info(f"response {custom_response}")


            except Exception as e:
                print("Error", e)
                return custom_response
        else:
            custom_response[section] = []
             
            
    return custom_response

async def check_grammar(sections, company):
    custom_response = {}
    for section, value in sections.items():
        logging.info(f"section {section}")
        if value:
            section_soup =  BeautifulSoup(value, 'html.parser')
            try:
                html_text = extract(section_soup)

                response = await client.chat.completions.create(
                    response_format={"type": "json_object"},
                    model="gpt-4o",
                    temperature = 0.2,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."
                        },
                        {
                            "role": "user",
                            "content": f'''Check the following page content for grammatical mistakes/errors (punctuation) and spelling Mistakes.
                            Company names such as this {company} should NOT be flagged as error.
                            Return a list of JSON objects, each containing the incorrect phrase, what the mistake is, and its corresponding sentence. 
                            Format the response as {{"mistakes": [{{"incorrect_phrase": "...", "reason": "..."}}, 
                            {{"incorrect_phrase": "...", "reason": "..."}}]}} ((The incorrect_phrase should be plain text and should contain 5-8 words of the sentence, not HTML)). 
                            The reason should be clear, as to what the problem is and where it is.
                            Only return actual errors such as: spelling, punctuation (missing commas, periods, etc.), and missing spaces.
                            If there is a period at the end of the sentence, do not flag it as an error. 
                            Always verify the JSON content twice before giving a response.
                            Page content: {html_text}'''
                        }
                    ],
                )
                response_text = response.choices[0].message.content.strip()
                filtered_response = json.loads(response_text)
                custom_response[section] = filtered_response
                logging.info(f"response {custom_response}")


            except Exception as e:
                print("Error", e)
                return custom_response
        else:
            custom_response[section] = []
    return custom_response
          

async def check_sections(sections):
    custom_response = {}
    for section, value in sections.items():
        logging.info(f"section {section}")
        if value:
            section_soup =  BeautifulSoup(value, 'html.parser')
            try:
                html_text = extract(section_soup)

                response = await client.chat.completions.create(
                    response_format={"type": "json_object"},
                    model="gpt-4o",
                    temperature = 0.1,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an assistant that strictly provides answers based only on the provided prompt and content."
                        },
                        {
                            "role": "user",
                            "content": (
                                f'''Check the following system description for the presence and quality of All the following sections 
                                    DC 1,
                                    DC 2,
                                    DC 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6
                                    DC 4,
                                    DC 5,
                                    DC 6,
                                    DC 7,
                                    DC 8,
                                    DC 9 '''
                                f"Ensure all sections from DC 1 to DC 9 mentioned above are present and that all those sections actually contain some information"
                                f"Return a list of missing sections and sections with no information at all. "
                                f"The reason can be Section is Missing or Information may not be valid and/or complete"
                                f'''Format the JSON response as mistakes: [{{"section": "...", "reason": "..."}}, {{"section": "...", "reason": "..."}}]'''
                                f"Page content: {html_text}"
                            )
                        }
                    ],
                )
                
                response_text = response.choices[0].message.content.strip()
                filtered_response = json.loads(response_text)
                custom_response[section] = filtered_response
                logging.info(f"response {custom_response}")


            except Exception as e:
                print("Error", e)
                return custom_response
        else:
            custom_response[section] = []
    return custom_response
          


async def check_infrastructure(sections, infrastructure_name):
    custom_response = {}
    for section, value in sections.items():
        logging.info(f"section {section}")
        if value:
            section_soup =  BeautifulSoup(value, 'html.parser')
            try:
                html_text = extract(section_soup)
             
                response = await client.chat.completions.create(
                    response_format={"type": "json_object"},
                    model="gpt-4o",
                    temperature = 0.2,
                    messages=[
                        {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
                        {"role": "user", "content": f'''Check if the primary infrastructure in cloud mentioned in  the following report content matches '{infrastructure_name}'. Some examples of primary infrastructures in cloud are AWS, Azure, GCP etc, so just try to look for cloud service providers such as those. If the infrastructure name does not match, return a list of JSON objects, each containing the incorrect infrastructure name and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as 'mistakes: [{{"incorrect_infrastructure": "...", "sentence": "..."}}]'. Find all the incorrect names and append the JSON to the list. Page content: {html_text}'''}
                    ]
                )

                response_text = response.choices[0].message.content.strip()
                filtered_response = json.loads(response_text)
                custom_response[section] = filtered_response
                logging.info(f"response {custom_response}")


            except Exception as e:
                print("Error", e)
                return custom_response
        else:
            custom_response[section] = []
    return custom_response