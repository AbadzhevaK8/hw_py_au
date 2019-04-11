#! python3
# multidownloadXkcd.py - загружает комиксы в несколько потоков.

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) # сохраняем комиксы в папке xkcd

def downloadXkcd(arg):
    pass
