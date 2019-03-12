#! python3
#! /usr/bin/python3
# -*- coding: utf-8 -*-
#renameDates.py - переименовывает файлы, имена которых включают даты, указанные в американском формате, приводя их в соответсвие с европейским форматом.

import shutil
import os
import re

# создание регулярного выражения, которому соответствуют имена файлов, содержащие даты в американском формате.

datePattern = re.compile(r"""^(.*?)
                         ((0|1)?\d)-
                         ((0|1|2|3)?\d)-
                         ((19|20)\d\d)
                         (.*?)$
                         """, re.VERBOSE)

# организация цикла по файлам в рабочем каталоге.
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)
    # пропуск файлов с именами, не содержащими дат.
    if mo == None:
        continue
    # получение отдельных частей имен файлов
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # формирование имен, соответсвующих европейскому стилю указания дат.
    euroFileName = beforePart + dayPart + '-' + \
        monthPart + '-' + yearPart + afterPart

    # получение полных абсолютных путей к файлам.
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # переименование файлов.
    print('Заменяем имя "%s" именем "%s"...' % (amerFileName, euroFileName))
    #shutil.move(amerFileName, euroFileName)
