import pyautogui
from time import sleep

pyautogui.click(964,543,duration=2)
pyautogui.write('yasmim')

pyautogui.click(972,576,duration=2)
pyautogui.write('2211')


pyautogui.click(846,610,duration=2)


with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
      produto = linha.split(',')[0]
      quantidade = linha.split(',')[1]
      preco = linha.split(',')[2]

      pyautogui.click(619,524,duration=2)
      pyautogui.write(produto)
    
    pyautogui.click(615,557,duration=2)
    pyautogui.write(quantidade)

    pyautogui.click(607,599,duration=2)
    pyautogui.write(preco)

    pyautogui.click(510,789,duration=1)
    sleep(1)
