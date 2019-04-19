#! python3

import pyautogui, time

time.sleep(5)
pyautogui.click() # щелчок для перевода фокуса в программу рисования

distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # сдвиг вправо
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) # сдвиг вниз
    pyautogui.dragRel(-distance, 0, duration=0.2) # сдвиг влево
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) # сдвиг вверх
