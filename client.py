import requests
from bs4 import BeautifulSoup

url = 'http://161.35.127.137:8000/service_check/Azure'
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
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One is an end-to-end advisory process automation platform that learns
    from working with human advisers and replicates tasks that do not require
    personal human interaction.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Its cognitive intelligence (the ‘bot’) streamlines the financial advisory
    processes, unlocking revenue and business growth potential. It enables
    seamless integration with the best advisory tools on the market to deliver
    clients the highest quality and value. The end-to-end unified experience,
    with a single point of digital interaction, strengthens the Financial
    Advisers' brands and reduces cybercrime risk.
  </p>

</div>
<div class="ql-tooltip ql-hidden">
  <a class="ql-preview" target="_blank" href="about:blank"></a
  ><input
    type="text"
    data-formula="e=mc^2"
    data-link="https://quilljs.com"
    data-video="Embed URL"
  /><a class="ql-action"></a><a class="ql-remove"></a>
</div>


'''


soup = BeautifulSoup(html_content, 'html.parser')

html_text = soup.get_text()

print(html_text)
# response = requests.post(url, data=html_content, headers={'Content-Type': 'text/html'})
# print(response.json())
