from selenium.webdriver import Firefox
from selenium import webdriver
from time import sleep

#PASSANDO A URL PARA UMA VARIAVEL
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

#PASSANDO O NAVEGADOR PRA UMA VARIÀVEL
navegador = Firefox()

#PASSANDO A URL PARA O NAVEGADOR
navegador.get(url)
#TEMPO PARA ESPERAR CARREGAR O CONTEÚDO DA PG
sleep(3)
#PEGANDO O CONTEúDO DA TAG 'H1'
titulo = navegador.find_elements_by_tag_name('h1')
#CRIANDO UM DICIONÁRIO
dc2 = {}




#JOGANDO OS ATRIBUTOS ENCONTRADO NA TAG 'p' PARA O DICIONARIO
for k in range(3):
     element = navegador.find_elements_by_tag_name('p')
     dc2.update({f'texto{k+1}': element[k].text})

#FECHANDO O NAVEGADOR
navegador.quit
#MOSTRANDO O DICIONARIO
print(dc2)