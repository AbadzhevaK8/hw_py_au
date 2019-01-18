#! /usr/bin/python3

catNames = []
while True:
    print('Введите имя кошки ' + str(len(catNames) + 1) + ' (Или ничего не вводите, чтобы остановиться.): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # добавление в список
print('Имена кошек: ')
for name in catNames:
    print(' ' + name)

input()
