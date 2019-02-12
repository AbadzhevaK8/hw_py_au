#! /usr/bin/python3

massage = 'It was a bright cold day in April, and the cloks were striking thirteen.'
count = {}

for character in massage:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

input()
