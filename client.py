import requests

url = 'http://161.35.127.137:8000/name_check/Zenith One'
html_content = '''
<div class="ql-editor" data-gramm="false" contenteditable="true">
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
      >DC 1: Company Overview and Types of Products and Services
      Provided</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd is a technology company headquartered in London, UK. The
    company's mission is to democratize financial advice by providing everyone
    globally with an AI Financial Advisor trained by the ablest Advisory
    professionals. This will help people make better financial decisions over
    their lifetime and build sustainable global wealth.
  </p>
 

'''

response = requests.post(url, data=html_content, headers={'Content-Type': 'text/html'})
print(response.json())
