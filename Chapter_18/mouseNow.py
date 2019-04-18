#! python3
# mouseNow.py - отображает текущую позицию указателя мышию

import pyautogui

print('Для выхода нажмите клавиши Ctrl+C.')
try:
    while True:
        # получить и вывести координаты курсора.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nГотово.')
