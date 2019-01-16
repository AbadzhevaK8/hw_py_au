#! /usr/bin/python3

import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Это точно.'
    elif answerNumber == 2:
        return 'Это решительно так.'
    elif answerNumber == 3:
        return 'Да.'
    elif answerNumber == 4:
        return 'Ответить смутно, попробуйте еще раз.'
    elif answerNumber == 5:
        return 'Спросите еще раз позже.'
    elif answerNumber == 6:
        return 'Сконцентрируйся и спроси снова.'
    elif answerNumber == 7:
        return 'Мой ответ - нет.'
    elif answerNumber == 8:
        return 'На вид не очень хорошо.'
    elif answerNumber == 9:
        return 'Очень сомнительно.'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
