#Importando Bibliotecas necessárias para abrir os navegadores
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome

#URL usada nos exemplos
url = "https://www.google.com/"

#Abrindo os navegadores e passando os mesmos para variáveis
browser = Firefox()
browser2 = Chrome()

#Abrindo os navegadores já em uma URL
browser.get(url)
browser2.get(url)
#Estamos passando o método 'get' para "pegarmos" a url e jogar para executar no nosso navegador

