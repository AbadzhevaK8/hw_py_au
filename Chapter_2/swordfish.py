#! /usr/bin/python3

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. Whar is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print ('Access granted.')
