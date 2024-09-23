import requests

url = 'http://161.35.127.137:8000/name_check/Zeneth One'
html_content = '''
<div class="ql-editor" data-gramm="false" contenteditable="true">
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
      >DC 1: Company Overview and Types of Products and Services
      Provided</strong
    >
  </h2>
 

'''

response = requests.post(url, data=html_content, headers={'Content-Type': 'text/html'})
print(response.json())
