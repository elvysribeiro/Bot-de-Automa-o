# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
     #"https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 2: Fazer login
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos
import pyautogui


pyautogui.PAUSE = 0.3


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write("link")