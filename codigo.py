# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
     #"https://dlp.hashtagtreinamentos.com/python/intensivao/login"

import pyautogui
import time

#  Abrir o chrome
pyautogui.PAUSE = .5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#  Esperar o site carregar
time.sleep(3)

#  Fazer o login
pyautogui.click(x=-964, y=405)
pyautogui.write("elvyssribeiro@gmail.com")

pyautogui.press("tab")
pyautogui.write("elvys_9035")

pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados de produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

     # Passo 4: Cadastrar 1 produto
     pyautogui.click(x=-967, y=280)

     codigo = tabela.loc[linha, "codigo"]

     # Preencher os campos
     pyautogui.write(str(tabela.loc[linha, "codigo"]))
     pyautogui.press("tab")

     pyautogui.write(str(tabela.loc[linha, "marca"]))
     pyautogui.press("tab")

     pyautogui.write(str(tabela.loc[linha, "tipo"]))
     pyautogui.press("tab")

     pyautogui.write(str(tabela.loc[linha, "categoria"]))
     pyautogui.press("tab")

     pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
     pyautogui.press("tab")

     pyautogui.write(str(tabela.loc[linha, "custo"]))
     pyautogui.press("tab")

     obs = tabela.loc[linha, "obs"]
     if not pandas.isna(obs):
          pyautogui.write(str(obs))
     
     # Apertar para enviar
     pyautogui.press("tab")
     pyautogui.press("enter") 
     pyautogui.scroll("50000")  

     # Passo 5: Repetir o cadastro para todos os produtos
