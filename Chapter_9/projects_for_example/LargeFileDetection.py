#! python3
# LargeFileDetection.py - просматривает каталог, ищет файлы размером более 100 МБ и выводит их на экран.

import os
import sys

# Получить каталог от пользователя
while True:
    userInput = input('Укажите папку для поиска:\n')
    if userInput.lower() == 'quit':
        sys.exit(1)
    else:
        userInput = os.path.abspath(userInput)
        if os.path.isdir(userInput):
            break
        else:
            print('Некорректный путь. Попробуйте еще. Введите "quit" для выхода.')
            continue

# Обход по каталогу добавляет файлы в список после сравнения.
largeFiles = []
number = 1
for folder, subfolders, filenames in os.walk(userInput):
    for filename in filenames:
        if os.path.getsize(os.path.join(folder, filename)) > 100e6:
            largeFiles.append((number,
                               '{} MB'.format(round(os.path.getsize(
                                   os.path.join(folder, filename)) / 1e6, 0)),
                               os.path.join(folder, filename)
                               ))
            number += 1

for file in largeFiles:
    print(file)
print('Готово.')
