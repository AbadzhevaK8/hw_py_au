#! python3
#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random
guess = ''
while guess not in ('орел', 'решка'):
    print('Угадайте результат подбрасывания монеты! Введите орел или решка:')
    guess = input()

toss = random.randint(0, 1)  # 0 - решка, 1 - орел

if toss == 0:
    toss = 'решка'
elif toss == 1:
    toss = 'орел'

if toss == guess:
    print('Есть!')
else:
    print('Увы! Попробуйте снова!')
    guess = input()
    if toss == guess:
        print('Есть!')
    else:
        print('Нет. Вам действительно не везет в этой игре!')
