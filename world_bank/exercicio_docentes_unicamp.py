from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://ic.unicamp.br/docentes/'

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

div_categorias_docentes = soup.findAll('div', {'class': 'cat-docente'})
print(div_categorias_docentes)

lista_categorias = [categoria.find('h3').text for categoria in div_categorias_docentes]
print(lista_categorias)

dados_professores = []

div_paineis_por_categoria = soup.findAll('div', {'class': 'grid-people'})

index_categoria = 0
for painel in div_paineis_por_categoria:
    div_people_item = painel.findAll('div', {'class': 'people-item'})

    for people_item in div_people_item:
        box = people_item.find('div', {'class': 'people-box'})
        box_div = box.find('div')
        box_name = box_div.find('h4', {'class': 'name'})

        nome_docente = box_name.find('a').text
        cargo = box_div.find('span', {'class':'cargo'}).text
        areas_pesquisa = [n.text for n in box_div.findAll('span', {'class':'nivel'})]

        dados_professores.append({'categoria':lista_categorias[index_categoria],'nome': nome_docente, 'cargo':cargo, 'areas_pesquisa':areas_pesquisa})
    
    index_categoria += 1

for dado in dados_professores:
    print('Categoria [{}] Nome: {} - Cargo: {} - Áreas de pesquisa: {}'.format(dado['categoria'], dado['nome'], dado['cargo'], dado['areas_pesquisa']))

#print(dados_professores)