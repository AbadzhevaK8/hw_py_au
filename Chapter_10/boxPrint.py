#! python3
#! /usr/bin/python3
# -*- coding: utf-8 -*-

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Переменная symbol должна быть односимвольной строкой.')
    if width <= 2:
        raise Exception('Значение width должно превышать 2.')
    if height <= 2:
        raise Exception('Значение height должно превышать 2.')
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
