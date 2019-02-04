#! /usr/bin/python3

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Введите имя питомца:')
name = input()
if name not in myPets:
    print('У меня нет питомца по имени ' + name)
else:
    print(name + ' это мой питомец.')

input()
