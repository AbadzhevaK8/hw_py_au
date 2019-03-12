#! python3
#! /usr/bin/python3
# -*- coding: utf-8 -*-
# backupToZip - копирует папку вместе со всем ее содержимым в zip-файл с инкременируемым номером копии файла.

import zipfile, os

def backupToZip(folder):
    # создание резервной копии всего содержимого папки "folder" в виде архива.
    folder = os.path.abspath(folder) # абсолютный путь к папке

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

    # TODO: добавить папку со всем содержимым в архив
    print('Готово.')

backupToZip ('C:\\путь_к_папке')
