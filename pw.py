#! python3
# password box
PASSWORDS = {'email': 'pa$$w0rD',
             'blog': 'Top$y_Cret',
             'luggage': 'parrrole'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Использование: python pw.py [account] - копирование пароля учетной записи')
    sys.exit()

account = sys.argv[1] #первый аргумент командной строки - это имя учетной записи

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + ' скопирован в буфер.')
else:
    print('Учетная запись ' + account + ' отсутствует в списке.')
