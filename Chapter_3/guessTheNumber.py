#! /usr/bin/python3

# Игра в угадывание чисел.

import random
secretNumber = random.randint(1, 100)
print('Мною задумано число от 1 до 100. Попробуйте его угадать.')

# Предоставить игроку 6 попыток для угадывания числа.

for guessesTaken in range(1, 7):
    print('Ваш вариант:')
    guess = int(input())

    if guess < secretNumber:
        print('Предложенное число меньше задуманного.')
    elif guess > secretNumber:
        print('Предложенное число больше задуманного.')
    else:
        break  # Соответствует правильному ответу!

if guess == secretNumber:
    print('Верно! Количество попыток: ' + str(guessesTaken))
else:
    print('Нет. Было задумано число ' + str(secretNumber))
