from openai import AzureOpenAI
import os
import json
from bs4 import BeautifulSoup
import re

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

def extract(soup):
    return '\n'.join([element.strip() for element in soup.stripped_strings])


async def check_company(html_text, company_name):
    soup = BeautifulSoup(html_text, 'html.parser')

    try:
        html_text = extract(soup)


        response = client.chat.completions.create(
            response_format={"type": "json_object"},
            model="gpt-4o",
            temperature = 0.3,
            messages=[
            {"role": "system", "content": "You are an assistant that matches text and strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
            {
                    "role": "user",
                    "content": (
                        f"Check the following system description for the name of the Company for which the system description is created"
                        f"Ensure the name mentioned in the conent is the same as {company_name}"
                        f"Return a list of incorrect names and misspelled names. "
                        f'''if the company name does not match, return a list of JSON objects, each containing the incorrect company name and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as 'mistakes: [{{"incorrect_company_name": "...", "sentence": "..."}}]'. Find all the incorrect names and append the JSON to the list. content : {html_text}'''
                    )
                }            
                ],
        )
        response_text = response.choices[0].message.content.strip()
        filtered_response = json.loads(response_text)


        return filtered_response
    except Exception as e:
        print("Error", e)
        return {"mistakes" : []}

async def check_date(html_text, start_date, end_date):
    soup = BeautifulSoup(html_text, 'html.parser')
    try:    
        html_text = extract(soup)


        response = client.chat.completions.create(
            response_format={"type": "json_object"},
            model="gpt-4o",
            temperature = 0.2,
            messages=[
                {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
                {"role": "user", "content": f'''Check if the start date and end date mentioned in the following page content match the given 
                 start date = {start_date} and end date = {end_date}. If there is a specific actual start date or end date mentioned in the content 
                 and it does not match the given dates, return a list of JSON objects. Each object should contain the incorrect date, the date format should not matter. If a specific date is not mentioned like the following : 2024-08-11, 11-08-24, 11-08-2024, 11 August 2024, it should not be flagged. 
                 Format the response as 'mistakes: [{{"incorrect_start_date": "...", "incorrect_end_date": "..."}}]'. 
                 Find all the incorrect dates and append each JSON object to the list. Page content: {html_text}'''}
            ],
        )
        response_text = response.choices[0].message.content.strip()
        filtered_response = json.loads(response_text)

        print(response_text)
        return filtered_response
    
    except Exception as e:
        print("Error", e)
        return {"mistakes" : []}

async def check_grammar(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    try:
        html_text = extract(soup)

        response = client.chat.completions.create(
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
                    Company names should NOT be flagged as error.
                    Return a list of JSON objects, each containing the incorrect phrase, what the mistake is, and its corresponding sentence. 
                    Format the response as mistakes: [{{"incorrect_phrase": "...", "reason": "...", "sentence" : "..."}}, 
                    {{"incorrect_phrase": "...", "reason": "...", "sentence" : "..."}}] ((The incorrect_phrase should be plain text and should contain 5-8 words of the sentence, not HTML)). 
                    The reason should be clear, as to what the problem is and where it is.
                    Only return actual errors such as: spelling, punctuation (missing commas, periods, etc.), and missing spaces.
                    If there is a period at the end of the sentence, do not flag it as an error. 
                    Page content: {html_text}'''
                }
            ],
        )
        response_text = response.choices[0].message.content.strip()
        filtered_response = json.loads(response_text)

        print(response_text)
        return filtered_response
    except Exception as e:
        print("Error", e)
        return {"mistakes" : []}

async def check_sections(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    try: 
        html_text = extract(soup)


        response = client.chat.completions.create(
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
                            DC 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7
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

        print(response_text)
        return filtered_response
    
    except Exception as e:
        print("Error", e)
        return {"mistakes" : []}


async def check_infrastructure(html_text, infrastructure_name):
    soup = BeautifulSoup(html_text, 'html.parser')
    try:
        html_text = extract(soup)

        response = client.chat.completions.create(
            response_format={"type": "json_object"},
            model="gpt-4o",
            temperature = 0.2,
            messages=[
                {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
                {"role": "user", "content": f'''Check if the primary infrastructure in cloud mentioned in Section 3.1 Primary Infrastructure of the following content matches '{infrastructure_name}'. Some examples of primary infrastructures in cloud are AWS, Azure, GCP etc, so just try to look for cloud service providers such as those. If the infrastructure name does not match, return a list of JSON objects, each containing the incorrect infrastructure name and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as 'mistakes: [{{"incorrect_infrastructure": "...", "sentence": "..."}}]'. Find all the incorrect names and append the JSON to the list. Page content: {html_text}'''}
            ]
        )

        response_text = response.choices[0].message.content.strip()
        filtered_response = json.loads(response_text)
        print(filtered_response)
        return filtered_response
    except Exception as e:
        print("Error", e)
        return {"mistakes" : []}