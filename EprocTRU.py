import time
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import lxml

def login(username, password):

  
    # Inicializa o navegador
    driver = webdriver.Chrome()

    # Abre a página de login
    driver.get("https://eproc.trf2.jus.br/eproc/")
   
    time.sleep(1)
    # Encontra os campos de login e senha
    username_input = driver.find_element(by=By.ID,value="txtUsuario")
    password_input = driver.find_element(by=By.ID,value="pwdSenha")

    # Preenche os campos de login e senha
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Clica no botão de login
    driver.find_element(by=By.ID,value="sbmEntrar").click()
    time.sleep(1)
    # Seleciona perfil do usuário
    perfil_input = driver.find_element(by=By.ID,value="tr1")
    perfil_input.click()
    time.sleep(4)
    #aciona menu dropdown
    seleciona_menu_dropdown = driver.find_element(by=By.CSS_SELECTOR, value="#main-menu > li:nth-child(5) > a > span.menu-item-text")
    seleciona_menu_dropdown.click()
    time.sleep(2)
    #Seleciona gerenciamento de processos
    seleciona_gerenciamento_processos = driver.find_element(by=By.CSS_SELECTOR, value="#menu-ul-38 > li:nth-child(1) > a > span.menu-item-text")
    seleciona_gerenciamento_processos.click()

    time.sleep(2)
    # define o dia de hoje e seleciona data de intimação
    currentDate = date.today().strftime("%d/%m/%Y")
    seleciona_data_intimacao = driver.find_element(by=By.ID, value="txtDataIntimacao")
    seleciona_data_intimacao.send_keys(currentDate)
    time.sleep(1)
    #seleciona órgãos julgadores
    seleciona_orgaos_julgadores = driver.find_element(by=By.CLASS_NAME,value="open")
    seleciona_orgaos_julgadores.click()
    time.sleep(1)
    escolhe_orgaos_julgadores = driver.find_element(by=By.CLASS_NAME, value="ms-search")
    escolhe_orgaos_julgadores.send_keys('TRU')
    time.sleep(1)
    seleciona_todos = driver.find_element(by=By.CLASS_NAME, value="ms-select-all")
    seleciona_todos.click()

    # faz consulta
    seleciona_botao_consulta = driver.find_element(by=By.CLASS_NAME, value= "btnConsultar")
    seleciona_botao_consulta.click()

    # Espera a página carregar
    time.sleep(5)
    print(today)

    # Encontra o título da página
    page_title = driver.title

    # Fecha o navegador
    #driver.quit()

    return page_title


if __name__ == "__main__":
    # Usuário e senha do sistema
    username = "g6274"
    password = "627235@Eproc"

    # Realiza o login
    page_title = login(username, password)

    # Imprime o título da página
    print(page_title)