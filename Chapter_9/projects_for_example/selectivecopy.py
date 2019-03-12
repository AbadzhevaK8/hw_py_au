#! python3
# selectivecopy.py - копирует все файлы с указанным расширением (например, .jpg или .pdf) через дерево каталогов в данный каталог.

import os
import shutil
import pprint

# TODO: Проверьте пути файлов, которые будут превышать максимальную длину в будущей версии.

# Получить расширение от пользователя
extensionInput = input('Укажите расширение (например: .pdf): ').strip('.')

# Получить исходную и целевую папку от пользователя
while True:
    sourceInput = os.path.abspath(input('Введите путь к папке для копирования:\n'))
    if os.path.exists(sourceInput):
        break
    else:
        print('Путь некорректный. Попробуйте еще. Введите ctrl-c для выхода.')
        continue
while True:
    destinationInput = os.path.abspath(input('Введите путь к папке назначения:\n'))
    if os.path.exists(destinationInput):
        break
    else:
        print('Путь некорректный. Попробуйте еще. Введите ctrl-c для выхода.')
        continue

# Построить список путей к файлам для копирования
copyList = []

for foldername, subfolders, filenames in os.walk(sourceInput):
    for filename in filenames:
        if str(filename).endswith(extensionInput):
            copyList.append(os.path.join(foldername, filename))

# Перебирайте список движущихся файлов.
print('Копирование этих файлов:')
pprint.pprint(copyList, width=200)


# Получить количество и размер всех файлов, которые будут скопированы (не требуется в описании проекта)
totalSize = 0
for file in copyList:
    totalSize += os.path.getsize(file)
print(str(len(copyList)) + ' файл(ов) будут скопированы. {} KB всего. Продолжить? [y/n]'.format(round(
    totalSize/1000, 0
)))
confirmInput = input()

if confirmInput.lower() in ['y', 'yes']:
    # Скопируйте список файлов по назначению
    for file in copyList:
        shutil.copy(file, destinationInput)
    print('Готово.')
elif confirmInput.lower() in ['n', 'no']:
    print('Отмена. Файлы не скопированы.')
else:
    print('Ввод не определен. Отмена операции.')
