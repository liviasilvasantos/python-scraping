from urllib.request import urlopen
from bs4 import BeautifulSoup
from scipy import stats

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

url = 'https://www.worldatlas.com/articles/the-25-largest-internet-companies-in-the-world.html'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

thead = soup.thead
linha_cabecalho = thead.find('tr')

colunas_cabecalho = linha_cabecalho.findAll('th')
colunas_cabecalho = [coluna.text for coluna in colunas_cabecalho]
print('Cabeçalho',colunas_cabecalho)

empresas = {}

tbody = soup.tbody

linhas = tbody.findAll('tr')

setores= []

for linha in linhas:
    colunas = linha.findAll('td')
    company  = colunas[1].text

    empresas[company] = {}
    empresas[company][colunas_cabecalho[0]] = colunas[0].text #rank
    empresas[company][colunas_cabecalho[2]] = colunas[2].text #industry
    empresas[company][colunas_cabecalho[3]] = colunas[3].text #revenue
    empresas[company][colunas_cabecalho[4]] = colunas[4].text #employees
    empresas[company][colunas_cabecalho[5]] = colunas[5].text #headquarters

    setor = colunas[2].text.lower()
    setores.append(setor)

print('Dados do facebook',empresas['Facebook'])

for k in empresas.keys():
    print('A empresa {} está em {}a. posição, já faturou {} bilhões de doláres'.format(k, empresas[k][colunas_cabecalho[0]], empresas[k][colunas_cabecalho[3]]))

setores_unicos = set(setores)
print(setores_unicos)    

frequencias = stats.itemfreq(setores)
print(frequencias)

freq = frequencias[:,1].astype(int)
print(freq)
xi = frequencias[:, 0]
print(xi)

fig = plt.figure(1)
x_pos = np.arange(len(xi))
plt.bar(x_pos, freq, align='center')
plt.ylim(0, max(freq)+ 0.5)
plt.xticks(np.arange(len(xi)), xi, rotation='vertical')
fig.autofmt_xdate()
plt.show()