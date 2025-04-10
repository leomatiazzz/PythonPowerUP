# Consulte o auxiliar.py para ir fazendo testes

import pyautogui
import time 

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> aperta 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.FAILSAFE = True

pyautogui.PAUSE = 0.5

#Passo 1: Entrar no site da empresa
pyautogui.press("win")
pyautogui.write("chrome") # ou qualquer outro browser
pyautogui.press("enter")

# digite o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(2)

#Passo 2: Fazer o login
# preencher o campo de email

#pyautogui.click(x=672, y=374) --> Método de clique também serve, mas achei menos prático
# O método click é muito arbitrário, depende da resolução da sua tela

pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")

# preencher o campo de senha
pyautogui.press("tab")
pyautogui.write("minhasenha123")

# botao logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar os produtos

for linha in tabela.index:

# É importante que nesse primeiro campo de digitação você use o método de click
# Testei com o método de pressionar tab e a automação começou a clicar em outros espaços do navegador
# Talvez tenha outro método que funcione no lugar, mas não procurei
    pyautogui.click(x=671, y=251)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.press("home")
 
