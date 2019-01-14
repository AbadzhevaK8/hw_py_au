#! /usr/bin/python3

import random

for i in range(5):
    print(random.randint(1, 10))

end_program = input()
if end_program == 0:
    print('Good bye!')
