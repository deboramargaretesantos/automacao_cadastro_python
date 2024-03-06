import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press ('win')
pyautogui.write ('chrome')
pyautogui.press ('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write (link)
pyautogui.press ('enter')

time.sleep (1)

pyautogui.click (x=513, y=372)
pyautogui.write('deborasantos@gmail.com')

pyautogui.click (x=559, y=465)
pyautogui.write('****')
pyautogui.press ('enter')

time.sleep (3)





