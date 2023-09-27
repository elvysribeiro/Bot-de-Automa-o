# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
     #"https://dlp.hashtagtreinamentos.com/python/intensivao/login"

import pyautogui
import time

#  Abrir o chrome
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#  entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#  Esperar o site carregar
time.sleep(3)

#  Fazer o login
pyautogui.click(x=375, y=611)
pyautogui.write("elvyssribeiro@gmail.com")


# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos