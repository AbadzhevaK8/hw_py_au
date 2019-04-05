#!python3
# removeCsvHeader.py - удаляет залоговки из всех csv-файлов в текущем рабочем каталоге.

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# цикл по всем файлам в текущем рабочем каталоге
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # пропускаем не csv
    print('Удаление заголовка из файла ' + csvFilename + '...')
    # прочитать csv-файл (с пропуском первой строки)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # пропустить первую строку
        csvRows.append(row)
    csvFileObj.close()
    # запись csv файла
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
