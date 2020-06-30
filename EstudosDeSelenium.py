from selenium.webdriver import Firefox
from time import sleep

#Passando a URL pra uma variável
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

#Passando o navegador a ser usado par auma variável
navegador = Firefox()
#Abrindo a Página
navegador.get(url)
#Esperando 3 segundos para carregar todos os elementos da página
sleep(3)

#utilizando o Find_element_by_tag_name para encontrar um elemento específico na página
a = navegador.find_element_by_tag_name('a')

#usando um for para pesquisar todos os elementos com a tag <p>
for click in range(11):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print (f'Valor do ultimo p {ps[-1].text} valor do click {click}')




navegador.quit()
