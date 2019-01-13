#! /usr/bin/python3
# Эта программа приветствует пользователя и запрашивает ввод информации

print ('Hello world!')
print ('What is your name?') # Запрос имени
myName = input()
print ('It is good to meet you, ' + myName)
print ('The lenght of your name is:')
print (len(myName))
print ('What is your age?') # Запрос возраста
myAge = input()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')
