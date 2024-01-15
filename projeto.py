import pyautogui
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 

pyautogui.write(link)

pyautogui.press('enter')

pyautogui.click(x=444, y=377)

pyautogui.write('camila14@gmail.com')

pyautogui.press('tab')

pyautogui.write('aSalto@123')

pyautogui.press('enter')

pyautogui.click(x=521, y=258)

import pandas
import time

tabela = pandas.read_csv('produtos.csv')
print(tabela)
for linha in tabela.index:

    codigo = tabela.loc[linha, 'codigo']

    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
         pyautogui.write(obs)
   
    
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)

    pyautogui.click(x=565, y=259)  
 












