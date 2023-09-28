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

#  entrar no link
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
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos