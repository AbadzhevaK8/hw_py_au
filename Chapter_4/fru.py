#! /usr/bin/python3

frutsList = ['apples', 'bananas', 'tofu', 'cats', 'hearts', 'tea']


def happy_list(l_name):
    fr_massage = ''
    for fruit in range(len(l_name) - 1):
        fr_massage += l_name[fruit] + ', '
    print(fr_massage + 'and ' + l_name[-1])

happy_list(frutsList)
