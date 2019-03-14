#! python3
#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Полпути пройдено!')
print('Орел выпал ' + str(heads) + ' раз.')
