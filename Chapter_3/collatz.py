#! /usr/bin/python3


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


while True:
    try:
        value = int(input("Введите число: "))
        break
    except ValueError:
        print("Введите целое число.")


while value != 1:
    print(collatz(value))
    value = collatz(value)
