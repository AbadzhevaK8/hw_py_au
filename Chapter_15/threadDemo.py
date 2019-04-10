#! python3

import threading
import time

print('Начало программы.')


def takeANap():
    time.sleep(5)
    print('Проснись!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('Конец программы.')
