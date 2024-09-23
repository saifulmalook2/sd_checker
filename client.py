import requests

url = 'http://127.0.0.1:8000/name_check'
html_content = '''
<div class="ql-editor" data-gramm="false" contenteditable="true">
  <h2><strong style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)">
    DC 1: Company Overview and Types of Products and Services Provided
  </strong></h2>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd is a technology company headquartered in London, UK.
  </p>
</div>
'''

response = requests.post(url, data=html_content, headers={'Content-Type': 'text/html'}, params={'company_name': 'Zenith One Ltd'})
print(response.json())
