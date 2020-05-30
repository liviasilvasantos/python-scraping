from urllib.request import urlopen
from bs4 import BeautifulSoup

#world development indicator: education inputs
url = 'http://wdi.worldbank.org/table/2.7'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

#existem dois elementos table com class indicators-table (uma no topo, e uma com os dados)
tabela = soup.findAll('table', {'class': 'indicators-table'})[1]

#cria uma lista com todas as linhas (tr) da tabela de dados
linhas = tabela.findAll('tr')

#cria um dicionario vazio de duas dimensoes {'pai': {'investimento':investimento, 'aluno_por_professor':qtde}}
dict = {}
#cria um dicionario vazio {'pais':investimento}
dict_investimento = {}

for linha in linhas:
    #recupera o conteúdo da primeira coluna com a class 'country'
    country = linha.find('td', { 'class' : 'country'}).text

    dict[country] = {}
    
    investimento = linha.findAll('td')[7].text
    dict[country]['investimento'] = investimento

    aluno_por_professor_pri = linha.findAll('td')[11].text
    dict[country]['alunos_por_professor_primario'] = aluno_por_professor_pri

    investimento_float = investimento
    if investimento_float == '..':
        investimento_float = '0'
    
    dict_investimento[country] = float(investimento_float)

print('Afghanistan', dict['Afghanistan']['investimento'], dict['Afghanistan']['alunos_por_professor_primario'])
print('Brasil', dict['Brazil']['investimento'], dict['Brazil']['alunos_por_professor_primario'])
print('Suíca', dict['Switzerland']['investimento'], dict['Switzerland']['alunos_por_professor_primario'])
print('Alemanha', dict['Germany']['investimento'], dict['Germany']['alunos_por_professor_primario'])
print('Japão', dict['Japan']['investimento'], dict['Japan']['alunos_por_professor_primario'])
print('Áustria - Investimento {} Qtde alunos por professor {}'.format(dict['Austria']['investimento'], dict['Austria']['alunos_por_professor_primario']))

#ordena os países pelo investimento, em ordem descrescente
paisesOrdenados = sorted(dict_investimento, key=dict_investimento.get, reverse=True)
print('País com maior investimento {}'.format(paisesOrdenados[0]))

#itera a lista ordenada exibindo a posicao ocupada por cada pais
for pais in paisesOrdenados:
    indice = paisesOrdenados.index(pais) + 1
    print(indice, pais)

#exibe a posicao ocupada pelo Brasil
print('Posição ocupada pelo Brasil: ', paisesOrdenados.index('Brazil') + 1)