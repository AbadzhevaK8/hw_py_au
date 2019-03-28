#!python3
# updateProduce.py - Корректирует цены в электронной таблице данных об объемах продаж.

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.get_sheet_by_name('Лист')

# Типы продукции и их обновленные цены.
PRICE_UPDATES = {'Лимон': 3.07,
                'Сельдерей': 1.19,
                'Чеснок': 1.27}

# TODO: создать цикл по строкам и обновить цены.
