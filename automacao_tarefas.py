import pyautogui            
import time

pyautogui.PAUSE = 0.5

pyautogui.press ('win') 
pyautogui.write ('chrome')
pyautogui.press ('enter') 


link = ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.write(str(link))
pyautogui.press('enter') 
time.sleep(3)

pyautogui.click(x=569, y=368)
pyautogui.write('deborasantos@gmail.com')
pyautogui.press('enter')
pyautogui.click(x=467, y=471)

pyautogui.write('****')
pyautogui.press('enter')

import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=597, y=261)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
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
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)






 


























