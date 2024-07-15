#bibliotecas necessárias: pyautogui | time | pandas (openpyxl numpy) | keyboard

import pyautogui 
import time 
import pandas

pyautogui.PAUSE = 1

#passo 1 - abrir o windows, acessar o chrome e entrar no site da empresa
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

#passo 2 - fazer o cadastro  
#clicar no campo de email
pyautogui.scroll(1000)
pyautogui.click(x=544, y=317)

#preencher email
pyautogui.hotkey('ctrl','a')
pyautogui.write('automacaopy@gmail.com')

#passar e preencher o campo de senha
pyautogui.press('tab')
pyautogui.write('minhaprimeiraautomacao')

#clicar no botão para entrar no cadastro
pyautogui.scroll(1000)
pyautogui.click(x=683, y=443)

time.sleep(3)

#Passo 3 - acessar a base de dados com os produtos

base_dados = pandas.read_csv('produtos.csv')

import keyboard

#Passo 4 - registrar os produtos 
for linha in base_dados.index:
    pyautogui.scroll(1000)

    #diminuir o tempo de pausa para cadastrar mais rápido       
    pyautogui.PAUSE = 0.5

    time.sleep(1)

    #checará se a tecla ESC foi pressionada
    if keyboard.is_pressed('esc'):
        #caso tenha sido pressionada, interromperá o loop 
        print('Processo interrompido pelo usuário')
        break

    #clicar no primeiro campo para escrever o código do produto
    pyautogui.click(x=492, y=227)

    #base_dados.loc[linha,coluna] - localiza o item pelo indice da linha e o nome da coluna
    pyautogui.write(str(base_dados.loc[linha,'codigo']))
    pyautogui.press('tab')

    pyautogui.write(str(base_dados.loc[linha,'marca']))
    pyautogui.press('tab')
 
    pyautogui.write(str(base_dados.loc[linha,'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(base_dados.loc[linha,'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(base_dados.loc[linha,'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(base_dados.loc[linha,'custo']))
    pyautogui.press('tab')

    obs = (str(base_dados.loc[linha,'obs']))
    if obs != 'nan': #se esse campo estiver vazio ele não irá preencher
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')





