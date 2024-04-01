# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pandas as pd
import pyautogui
import time

# pyautogui.write -> para escrever
# pyautogui.press -> para fazer o input de uma tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas "CTRL+C"

pyautogui.PAUSE = 0.3 # Define um tempo de espera para realizar a próxima ação. Este PAUSE funcione globalmente.

# Para abrir o App (Neste caso o Chrome.)

pyautogui.press("win") # Faz o input da tecla "Windows"
pyautogui.write("chrome") # Aqui irá escrever "Chrome" na barra de pesquisa do windows.
pyautogui.press("enter") # Faz o input da tecla "Enter"
time.sleep(3)
# Passo a Passo para entrar no Sistema da Empresa:

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Realizar o login

pyautogui.click(x=665, y=453) # Nesta etapa selecionamos as coordenadas de onde deverá ser realizado o clique.
# Interessante nessa ocasião ter um arquivo extra apenas para extrair a coordenada com exatidão.
# Neste caso o arquivo > pegar_posicao.py

# Passo 2:Processo para fazer login
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # Pula para o próximo campo com essa tecla.
pyautogui.write("sua senha")
pyautogui.click(x=960, y=662)
time.sleep(3)


# Passo 3: Importar a base de produtos para cadastrar

tabela = pd.read_csv("produtos.csv")

# Passo 4: Laço para cadastro de Produtos

for linha in tabela.index:
    pyautogui.click(x=967, y=314)       # Seleciona o primeiro campo para preencher o cadastro.
    codigo = tabela.loc[linha, "codigo"]# Puxa da tabela o valor da linha Código.
    pyautogui.write(str(codigo))
    pyautogui.press("tab")              # Pula para o próximo campo

    # Este algoritmo se repete para as outras linhas da tabela, até preencher todo o cadastro.
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
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        time.sleep(1)
    pyautogui.press("enter") # Com este 'enter' você termina de cadastrar o produto.

    pyautogui.scroll(5000) # Sob a página para continuar o cadastro