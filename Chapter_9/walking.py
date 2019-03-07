#! python3

import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\AbadzhevaE\\delicious'):
    print('Текущая папка — ' + folderName)

    for subfolder in subfolders:
        print('Подпапка ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('Файл внутри ' + folderName + ': '+ filename)

    print('')
