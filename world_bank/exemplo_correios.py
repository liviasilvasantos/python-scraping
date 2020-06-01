import requests
from bs4 import BeautifulSoup

url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'

objetos = {'objetos':'PY136072214BR'}

html = requests.post(url=url, data=objetos)

soup = BeautifulSoup(html.text, 'html.parser')
print(soup.strong.text)
