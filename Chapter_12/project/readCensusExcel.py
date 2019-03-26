#!python3
# -*- coding: utf-8 -*-
# readCensusExcel.py - формирует таблицу данных о численности населения и количестве переписных районов в каждом округе.

import openpyxl
import pprint

print('Открытие рабочей книги...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Чтение строк...')
for row in range(2, sheet.max_row + 1):
    # В каждой строке электронной таблицы содержатся данные для одного переписного района.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Гаранития существования ключа для данного штата.
    countyData.setdefault(state, {})
    # Гаранития существования ключа для данного округа данного штата.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    #  Каждая строка представляет один переписной район, поэтому инкременируем на единицу.
    countyData[state][county]['tracts'] += 1
    # Увеличиваем численность населения округа на численность населения переписного района.
    countyData[state][county]['pop'] += int(pop)

# открытие нового текстового файла и запись в него содержимого словаря countyData
print('Запись результатов...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Готово.')
