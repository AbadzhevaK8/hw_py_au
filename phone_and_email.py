#python3
#phone_and_email.py - Находит телефонные номера и адреса электронной почты

import pyperclip, re
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # американский зип-код
    (\s|-|\.)?                          # разделитель
    (\d{3})                             # первые три цифры
    (\s|-|\.)                           # разделитель
    (\d{4})                             # последние 4 цифры
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # добавочный номер
    )''', re.VERBOSE)

# создать регэкс для адресов электронной почты
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # имя пользователя
    @                                   # собака
    [a-zA-Z0-9.-]+                      # домен
    (\.[a-zA-Z]{2,4})                   # домен верхнего уровня
    )''', re.VERBOSE)

# найти соответствия в тексте, содержащемся в буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num+=' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# TODO: скопировать результаты в буфер обмена

# дома допишу
# Если спать не упаду
