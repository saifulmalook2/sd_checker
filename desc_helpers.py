import os
import logging
import pathlib
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import CSVLoader
import pandas as pd
from docx import Document as DocxDocument
from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader
from openai import AsyncAzureOpenAI
import json
import tiktoken

logging.basicConfig(format="%(levelname)s     %(message)s", level=logging.INFO)
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)

encoding = tiktoken.encoding_for_model("gpt-4o")


async def docx_loader(file):
    docx = DocxDocument(file)
    paragraphs = [
        paragraph.text for paragraph in docx.paragraphs if paragraph.text.strip()
    ]  # Skip empty paragraphs
    return paragraphs


async def excel_loader(file):
    sheets = pd.read_excel(file, sheet_name=None)
    rows = []

    for sheet_name, df in sheets.items():
        for _, row in df.iterrows():
            row_text = " ".join(
                str(cell) for cell in row if pd.notna(cell)
            )  # Skip NaN values
            rows.append(row_text)

    return rows


async def load_pdf(file_path: str):
    # Load the PDF using PyPDFLoader
    pdf_loader = PyPDFLoader(file_path)

    # Extract all pages as separate elements
    pages = pdf_loader.load()

    # Create a list of strings, each containing the content of one page
    page_contents = [page.page_content for page in pages]

    return page_contents


async def load_csv(file_path: str):
    # Load the CSV file using pandas
    df = pd.read_csv(file_path)

    # Create a list of strings, each containing the content of one row
    row_contents = [", ".join(map(str, row)) for row in df.values]

    return row_contents


async def process_file(filenames):

    try:
        all_documents = {}

        # File path where the docs are stored
        files = os.path.join(os.getcwd(), "docs")

        # Process each file in a thread pool (for CPU-bound tasks)
        for filename in filenames:
            file = os.path.abspath(os.path.join(files, filename))
            logging.info(f"Processing {file}")

            file_extension = pathlib.Path(file).suffix

            # Depending on file type, handle parsing (can include CPU-bound operations)
            if file_extension.lower() == ".pdf":
                raw_documents = await load_pdf(file)
                all_documents[filename] = raw_documents

            elif file_extension.lower() == ".xlsx":
                raw_documents = await excel_loader(
                    file
                )  # Handle async inside sync context
                all_documents[filename] = raw_documents

            elif file_extension.lower() == ".csv":
                raw_documents = await load_csv(file)
                all_documents[filename] = raw_documents

            elif file_extension.lower() == ".docx":
                raw_documents = await docx_loader(file)
                all_documents[filename] = raw_documents

            elif file_extension.lower() in [".jpg", ".jpeg", ".png"]:
                raw_documents = AzureAIDocumentIntelligenceLoader(
                    api_endpoint=os.getenv("IMAGE_LOADER_ENDPOINT"),
                    api_key=os.getenv("IMAGE_LOADER_KEY"),
                    file_path=file,
                    mode="page",
                ).load()
                raw_documents = raw_documents[0].page_content
                all_documents[filename] = [raw_documents]

        # print(all_documents)

        return all_documents

    except Exception as e:
        logging.error(f"Error in load_data: {e}")
        return False


client = AsyncAzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)


async def verify_control(contents, control,start_date, end_date):
    response = await client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        temperature=0.5,
        messages=[
            {
                "role": "system",
                "content": "You are an expert SOC Auditor. Your role is to evaluate evidence and policy file contents provided to you, determining if they satisfy the specified controls. Base your judgments strictly on the provided content, without speculation, hallucination, or outside information.",
            },
            {
                "role": "user",
                "content": (
                    f"Please evaluate the following file contents in relation to the specified control: '{control}', if the control requires a time range for the evidence provided then also confirm that the evidence fall with the following start date = {start_date} and end date = {end_date}. "
                    f"Your task is to determine whether the evidence provided demonstrates compliance with the requirements of this control. "
                    f"Carefully analyze the content for relevant policies, procedures, or documentation that would indicate adherence to the control. "
                    f"Some controls do not require any evidence, they can be satisfied solely by the policy files "
                    f"In your response, provide a JSON object structured as follows: "
                    f"{{ 'message': '...', 'reason': '...' }}. "
                    f"1. If the control is satisfied, clearly state that it is satisfied and provide a detailed reason explaining how the evidence supports compliance. "
                    f"2. If the control is not satisfied, indicate that it is not satisfied and provide a specific reason outlining the deficiencies or lack of evidence related to the control requirements. "
                    f"3. The message and the reason should be 2-3 sentences each, covering the details and specfic information that was used to come to the conclusion regarding the evidence."
                    f"Make sure your analysis is thorough and directly linked to the content provided. "
                    f"The content I am providing with be filenames (which can be a policy file or an evidence file), with their respective text content."
                    f"Content: {contents}"
                ),
            },
        ],
    )
    response_text = response.choices[0].message.content.strip()
    filtered_response = json.loads(response_text)

    return filtered_response
