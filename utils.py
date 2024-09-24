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
    response = client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        messages=[
         {"role": "system", "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."},
        {"role": "user", "content": f"Check if the company mentioned in the following page content matches '{company_name}'. If the company name mentioned does not match, return a list of JSON objects, each containing the incorrect company name and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as mistakes : [{{'incorrect_name': '...', 'sentence': '...'}}, {{'incorrect_name': '...', 'sentence': '...'}}]. Find all the incorrect names and append the JSON to the list. Page content: {html_text}"}
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
            {"role": "user", "content": f"Check if the date mentioned in the following page content matches '{given_date}'. If the date mentioned does not match, return a list of JSON objects, each containing the incorrect date and the sentence it is mentioned in (The sentence should be plain text, not HTML). Format the response as mistakes: [{{'incorrect_date': '...', 'sentence': '...'}}, {{'incorrect_date': '...', 'sentence': '...'}}]. Find all the incorrect dates and append the JSON to the list. Page content: {html_text}"}
        ],
    )
    response_text = response.choices[0].message.content.strip()
    filtered_response = json.loads(response_text)

    print(response_text)
    return filtered_response

async def check_grammar(html_text):
    response = client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate, hallucinate, or provide information not directly found in the content."
            },
            {
                "role": "user",
                "content": f"Check the following page content for grammar mistakes (punctuation and typos). Return a list of JSON objects, each containing the incorrect phrase and what the mistake is. Format the response as mistakes: [{{'incorrect_phrase': '...', 'reason': '...'}}, {{'incorrect_phrase': '...', 'reason': '...'}}] ((The sentence should be plain text, not HTML)). Page content: {html_text}"
            }
        ],
    )
    response_text = response.choices[0].message.content.strip()
    filtered_response = json.loads(response_text)

    print(response_text)
    return filtered_response


template_sd = '''
DC 1: Company overview and types of products and services provided 
<Delete me: Insert your company background from your website, marketing brochures, client presentation, LinkedIn etc.>
DC 2: The principal service commitments and system requirements
<Delete me: Service commitments may be communicated to user entities in many ways and found in customer contracts, service level agreements (SLA), user guides and feature list and published policies, (for example, a privacy or security policy). No specific form of communication is required. 
 
[Add additional security commitments made to customers as necessary]
[Add availability commitments made to customers if the report includes the Availability TSC]
[Add confidentiality commitments made to customers if the report includes the Confidentiality TSC]
[Add processing integrity commitments made to customers if report includes the Processing Integrity TSC]
[Add privacy commitments made to customers if the report includes the Privacy TSC]>
<Delete me: Principal System Requirements are specified in the service organization’s system policies, standards and procedures, system design documentation, contracts with customers, laws, government regulations and guidelines of industry groups (NIST 800-53 standards, PCI DSS), such as business or trade associations. You can also paste a link to your specification/implementation documentation sites here.>
 

DC 3: The components of the system used to provide the services

3.1 Primary Infrastructure and Applications:
<Delete Me: Provide a table like the one shown that includes the company’s application and infrastructure components. Include physical or virtual resources that support the overall IT environment. Please also provide a systems and network architecture diagram if any.>
Application/System	Process/Transactions	Purchased or Developed	Platform and Operating System	Datastore	Data Type
Delete Me: Custom HR System	Delete Me: Employee records and HR processes	Delete Me: Developed	Delete Me: Linux, Ubuntu	Delete Me: MySQL	Delete Me: Employee information, payroll data

3.3 People:
<Delete Me: Please upload an organization chart if you have any. Define roles and responsibilities for the people components, including personnel involved in the governance, management, business operation, sales, marketing, and security. Include use of the primary system business unit personnel, developers, devops, customer success, IT support, and training.>

3.4 Security Processes and Procedures: 
<Delete Me: Please outline the company’s procedures from the Information Security Policy.>

3.5 Data: 
<Delete Me: Please upload a data flow diagram tracing customer data as it travels to and from your company if you have any, or define the data types and how you protect them as documented in the Data Management Policy.>

3.6 Third Party Access: 
<Delete Me: List out the company’s vendors, SAAS tools, business partners, and other third parties that often store, process, and transmit sensitive data or otherwise access the service organization’s system. These third parties may provide components of the system. Service organization management may need to describe the components of the system provided by such third parties. Such disclosures may include, for example, the nature of the third parties’ access and connectivity to the service organization's system.>

3.7 System Boundaries: (Product lines/ LOBs/ brands)
<Delete Me: List of systems and business processes that are within the boundaries of the description of the system in scope here>

DC 4: Disclosures about identified security incidents 
<Delete Me: Provide breach notifications for any identified system incidents that (a) were the result of controls that were not suitably designed or operating effectively, or (b) otherwise resulted in a significant failure in the achievement of one or more of those service commitments and system requirements in last 12 months, as of the date of the description (for a type 1 audit), or during the period of time covered by the description (for a type 2 audit), as applicable.>

DC 5: The applicable trust services criteria and the related controls designed to provide reasonable assurance that the service organization’s service commitments and system requirements were achieved
<Delete me: Under this section of the system description, describe briefly the process and procedures in place for each unique control in scope, include who, what, where, when, and why. Add the relevant control ID to each process and procedure to show which control it maps to. For example:
DC 6: Complementary User Entity Controls (CUECs):
ABC’s services are designed with the assumption that certain controls will be implemented by user entities. Such controls are called complementary user entity controls. It is not feasible for all the Trust Services Criteria related to ABC’s services to be solely achieved by ABC’s control procedures. Accordingly, user entities, in conjunction with the services, should establish their own internal controls or procedures to complement those of ABC. 
The following complementary user entity controls should be implemented by user entities to provide additional assurance that the Trust Services Criteria described within this report are met. As these items represent only a part of the control considerations that might be pertinent at the user entities’ locations, user entities’ auditors should exercise judgment in selecting and reviewing these complementary user entity controls.
DC 7: Complementary Subservice Organization Controls (CSOCs): <Delete me: Please change the name of the cloud service provider from AWS to yours> 
Although the subservice organization has been “carved out” for the purposes of this report, certain Trust Services Criteria are intended to be met by controls at the subservice organization. Complementary Subservice Organization Controls (CSOCs) are expected to be in place at AWS related to physical security and environmental protection, as well as backup, recovery, and redundancy controls related to availability. AWS physical security controls mitigate the risk of fires, power loss, climate, and temperature variabilities. Management of ABC receives and reviews the AWS SOC 2 report annually. In addition, through its operational activities, ABC management monitors the services performed by AWS to determine whether operations and controls expected to be implemented at the subservice organization are functioning effectively. Management also has communication with the subservice organization to monitor compliance with the service agreement, stay abreast of changes planned at the hosting facility, and relay any issues or concerns to AWS/Google/Azure management. 
It is not feasible for the criteria related to the System to be achieved solely by ABC. Therefore, each user entity's internal control must be evaluated in conjunction with ABC’s controls and related tests, and results described in Section 4 of this report, considering the related CSOCs expected to be implemented at the subservice organization as described below.
DC 8: Disclosures of out of scope Trust Services Criteria
<Delete me: If one or more applicable trust services criteria are not relevant to the system being described, service organization management includes here an explanation of why such criteria are not relevant. For example, physical and environmental security criteria may be descoped for fully virtual and remote companies.>

DC 9: Disclosures of significant changes in last 1 year
<Delete me: Examples of significant changes to a system include the following:
●	Changes to the services provided
●	Significant changes to IT and security personnel
●	Significant changes to system processes, IT architecture and applications, and the processes and system used by subservice organizations
●	Changes to legal and regulatory requirements that could affect system requirements
●	Changes to organizational structure resulting in a change to internal control over the system (for example, a change to the legal entity)>
●	

'''

async def check_sections(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    html_text = soup.get_text()

    response = client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that strictly provides answers based only on the provided content. Do not speculate or provide information not directly found in the content."
            },
            {
                "role": "user",
                "content": (
                    f"Check the following system description for the presence and quality of sections DC1 to DC9. "
                    f"Ensure all sections are present and that none use templated language from this template {template_sd}. "
                    f"Return a list of missing sections and sections with templated language. "
                    f"Format the JSON response as mistakes: [{{'incorrect_section': '...', 'reason': '...'}}, {{'incorrect_section': '...', 'reason': '...'}}]"
                    f"Page content: {html_text}"
                )
            }
        ],
    )
    
    print(response)
    response_text = response.choices[0].message.content.strip()
    filtered_response = json.loads(response_text)

    print(response_text)
    return filtered_response