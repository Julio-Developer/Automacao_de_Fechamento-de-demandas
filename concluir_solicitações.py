# -*- coding: utf-8 -*-

# Esse programa deve usar o selenium, abrir um determiado site, fazer o login e cancelar as solicitações seguindo uma regra determinda.

# importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
import os
import sys


# Dados do programa
# ----------------- # 

# recebendo senha e usuario
usuario = input("Digite o usuario: ")
senha_usuario = input("Digite a senha do usuario: ")


# Site a ser aberto
site = "https://garcia.xpro.me/dashboard"


# campo_senha
campo_email = '//*[@id="login"]/input'


# campo senha
campo_senha = '//*[@id="exampleInputPassword2"]'


# campo solicitacoes
campo_solicitcoes = '//*[@id="nav-accordion"]/li[3]/a/span[1]'


# campo atendimetnos 
campo_atendimentos = '//*[@id="nav-accordion"]/li[3]/ul/li[1]/a'


# Botão filtro
filtro_telefonia = '//*[@id="main-content"]/section/div/div[1]/div/section/div/div/div/div/div/a[1]'


# lista quantidade de solicitações na tela
quatidade_solicitacoes_tela = '//*[@id="leads-table_length"]/label/select'
quantidade = '//*[@id="leads-table_length"]/label/select/option[4]'


# botão selecionar todos
selecionar_todos = '//*[@id="leads-table"]/thead/tr/th[1]/div/div'


# botão alterar solicitacao
alterar_solicitacao = '//*[@id="tab-lista"]/div[1]/button'
botao_alterar = '//*[@id="alterarcadastro"]'


# botão cancelar solicitacao
cancelar_solicitacao = '//*[@id="s2id_statusalterar"]/a/span[2]/b'
botao_cancelar = '//*[@id="select2-results-6"]/li[7]'


# botão confirmar
confirmar_cancelamento = '//*[@id="botaoalterarleads"]'


# quantidade de solicitacoes
quantidade_solicitacoes_total = 2


#################################################

# Função limpa tela

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpar()
# abrindo o navegador
browser = webdriver.Chrome()
print('Abrindo o navegador\n')
sl(1)


# abrindo o site
browser.get(site)
print('Abrindo o site\n')
sl(1)


# passando senha e email
browser.find_element('xpath', campo_email).send_keys(usuario)
print('Logando\n')


# passando senha
browser.find_element('xpath', campo_senha).send_keys(senha_usuario)
print('Logando\n')


# apertando enter
browser.find_element('xpath', campo_senha).send_keys(Keys.ENTER)
print('Login\n')
sl(1)
limpar()


# rotina solicitacoes e clicar no botao
browser.find_element('xpath', campo_solicitcoes).click()
print('Procurando Campo Solicitações\n')



# atendimentos
browser.find_element('xpath', campo_atendimentos).click()
print('Procurando Campo Solicitações\n')


# Apertando no botão de filtro
browser.find_element('xpath', filtro_telefonia).click()
print('Aplicando Filtro\n')
sl(5)
limpar()


# Mudando a quantidade de visualizaçào
browser.find_element('xpath', quatidade_solicitacoes_tela).click()
print('Quantidade de Solicitações\n')
sl(1)
browser.find_element('xpath', quantidade).click()
print('Definindo a quantidade de solicitaçòes\n')
sl(1)


# REcarregando a pagina
browser.refresh()
print('Recarregando a página\n')
sl(15)
limpar()


while quantidade_solicitacoes_total != 0:


    # selecionando todas
    browser.find_element('xpath', selecionar_todos).click()
    print('Selecionando as solicitações\n')
    sl(3)


    # alterar solicitacao
    browser.find_element('xpath', alterar_solicitacao).click()
    print('Botão alterar\n')
    sl(1)


    # alterar o status
    browser.find_element('xpath', botao_alterar).click()
    print('Alterar\n')
    sl(1)


    # selecionando o status
    browser.find_element('xpath', cancelar_solicitacao).click()
    print('Seleção de cancelamento\n')
    sl(1)


    browser.find_element('xpath', botao_cancelar).click()
    print('Cancelar\n')
    sl(1)


    # confirmar
    browser.find_element('xpath', confirmar_cancelamento).click()
    print('Confirmar cancelamento\n')
    print('Processando...\n')
    sl(95)


    # Recarregando a pagina
    browser.refresh()
    print('Recarregar Pagina\n')
    sl(10)
    limpar()


    # solicitaçòes restantes 
    quantidade_solicitacoes_total -= 1
    print(f'Quantidade de repetições restantes {quantidade_solicitacoes_total}\n')
