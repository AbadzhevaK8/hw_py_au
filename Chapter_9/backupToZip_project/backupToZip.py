#! python3
#! /usr/bin/python3
# -*- coding: utf-8 -*-
# backupToZip - копирует папку вместе со всем ее содержимым в zip-файл с инкременируемым номером копии файла.

import zipfile
import os


def backupToZip(folder):
    
    # создание резервной копии всего содержимого папки "folder" в виде архива.
    folder = os.path.abspath(folder)  # абсолютный путь к папке

    # определяем,как надо назвать архив
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    # создаем файл архива
    print('Создается файл %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # добавить папку со всем содержимым в архив
    for foldername, subfolders, filenames in os.walk(folder):
        print('Добавление файлов из папки %s...' % (foldername))
        # добавить в архив текущую папку.
        backupZip.write(foldername)
        # в архив все файлы из данной папки.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # не создавать резервные копии самих архивов.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Готово.')


backupToZip('C:\\Users\\AbadzhevaE\\Downloads\\hw_py_au\\Chapter_9')
