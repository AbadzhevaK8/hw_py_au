#! /usr/bin/python3


def spam():
    eggs = 'spam local'
    print(eggs)  # выводится строка spam local


def bacon():
    eggs = 'bacon local'
    print(eggs)  # выводится строка bacon local
    spam()
    print(eggs)  # выводится строка bacon local


eggs = 'global'
bacon()
print(eggs)  # выводится строка global
