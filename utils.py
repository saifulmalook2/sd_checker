from openai import AzureOpenAI
import os
import json

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

async def check_company(html_text, company_name):
    response = client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        messages=[
         {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
        {"role": "user", "content": f"Check if the company mentioned in the following page content matches '{company_name}'. If the company name mentioned does not match, return a list of JSON objects, each containing the incorrect company name and the sentence it is mentioned in. Format the response as mistakes : [{{'incorrect_name': '...', 'sentence': '...'}}, {{'incorrect_name': '...', 'sentence': '...'}}]. Find all the incorrect names and append the JSON to the list. Page content: {html_text}"}
        ],
    )

    response_text = response.choices[0].message.content.strip()
    filtered_response = json.loads(response_text)

    return filtered_response

async def check_date(html_text, given_date):
    response = client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
            {"role": "user", "content": f"Check if the date mentioned in the following page content matches '{given_date}'. If the date mentioned does not match, return a list of JSON objects, each containing the incorrect date and the sentence it is mentioned in. Format the response as mistakes: [{{'incorrect_date': '...', 'sentence': '...'}}, {{'incorrect_date': '...', 'sentence': '...'}}]. Find all the incorrect dates and append the JSON to the list. Page content: {html_text}"}
        ],
    )
    response_text = response.choices[0].message.content.strip()
    filtered_response = json.loads(response_text)

    print(response_text)
    return filtered_response

