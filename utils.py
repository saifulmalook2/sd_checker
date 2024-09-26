from openai import AzureOpenAI
import os
import json
from bs4 import BeautifulSoup

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

async def check_company(html_text, company_name):
    soup = BeautifulSoup(html_text, 'html.parser')
    try:
        html_text = soup.get_text()

        response = client.chat.completions.create(
            response_format={"type": "json_object"},
            model="gpt-4o",
            temperature = 0.2,
            messages=[
            {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
            {"role": "user", "content": f"Check if the company mentioned in the following page content matches '{company_name}' (Ignore any special characters in the name). If the company name mentioned does not match, return a list of JSON objects, each containing the incorrect company name and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as mistakes : [{{'incorrect_name': '...', 'sentence': '...'}}, {{'incorrect_name': '...', 'sentence': '...'}}]. Find all the incorrect names and append the JSON to the list. Short forms or abbreviations of the name are not mistakes. Page content: {html_text}"}            ],
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
        html_text = soup.get_text()

        response = client.chat.completions.create(
            response_format={"type": "json_object"},
            model="gpt-4o",
            temperature = 0.2,
            messages=[
                {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
                {"role": "user", "content": f"Check if the start date and end date mentioned in the following page content match the given start date = {start_date} and end date = {end_date}. If there is a specific actual start date or end date mentioned in the content and it does not match the given dates, return a list of JSON objects. Each object should contain the incorrect date and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as 'mistakes: [{{'incorrect_date': '...', 'sentence': '...'}}]'. Find all the incorrect dates and append each JSON object to the list. Page content: {html_text}"}
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
        html_text = soup.get_text()

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
                    "content": f"Check the following page content for grammatical mistakes/errors (punctuation) and spelling Mistakes. Return a list of JSON objects, each containing the incorrect phrase, what the mistake is, and its corresponding sentence. Format the response as mistakes: [{{'incorrect_phrase': '...', 'reason': '...'}}, {{'incorrect_phrase': '...', 'reason': '...'}}] ((The sentence should be plain text, not HTML)). Page content: {html_text}"
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
        html_text = soup.get_text()

        response = client.chat.completions.create(
            response_format={"type": "json_object"},
            model="gpt-4o",
            temperature = 0.2,
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that strictly provides answers based only on the provided prompt and content."
                },
                {
                    "role": "user",
                    "content": (
                        f"Check the following system description for the presence and quality of sections DC 1, DC 2, DC 3, DC 4, DC 5, DC 6, DC 7, DC 8, DC 9. "
                        f"Ensure all sections from DC 1 to DC 9 are present and that all those sections actually contain some information"
                        f"Return a list of missing sections and sections with no information at all. "
                        f"The reason can be Section is Missing or Information may not be valid and/or complete"
                        f"Format the JSON response as mistakes: [{{'section': '...', 'reason': '...'}}, {{'section': '...', 'reason': '...'}}]"
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
        html_text = soup.get_text()

        response = client.chat.completions.create(
            response_format={"type": "json_object"},
            model="gpt-4o",
            temperature = 0.2,
            messages=[
                {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
                {"role": "user", "content": f"Check if the primary infrastructure in cloud mentioned in section 3.1 of the following page content matches '{infrastructure_name}'. Some examples of primary infrastructures in cloud are AWS, Azure, GCP etc, so just try to look for cloud service providers such as those. If the infrastructure name does not match, return a list of JSON objects, each containing the incorrect infrastructure name and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as 'mistakes: [{{'incorrect_name': '...', 'sentence': '...'}}]'. Find all the incorrect names and append the JSON to the list. Page content: {html_text}"}
            ]
        )

        response_text = response.choices[0].message.content.strip()
        filtered_response = json.loads(response_text)
        print(filtered_response)
        return filtered_response
    except Exception as e:
        print("Error", e)
        return {"mistakes" : []}