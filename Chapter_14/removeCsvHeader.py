#!python3
# removeCsvHeader.py - удаляет залоговки из всех csv-файлов в текущем рабочем каталоге.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# цикл по всем файлам в текущем рабочем каталоге
for csvFilename in os.listdir('.'):
    if not csvFilename.endwith('.csv'):
        continue # пропускаем не csv
    print('Удаление заголовка из файла ' + csvFilename + '...')

# TODO: 
