#! python3
# stopWatch.py - простая программа-хронометр

import time

# отображение инструкции по использованию программы.
print('Чтобы начать отсчет, нажмите клавишу ENTER. Впоследствии для имитации щелчков кнопки секундомера нажимайте клавишу ENTER. Для выхода из программы нажмите клавиши Ctrl+C.')
input()  # нажатие клавиши enter начинает отсчет
print('Отсчет начат.')
startTime = time.time()  # получение времени начала первого замера
lastTime = startTime
lapNum = 1

# начало отслеживания замеров
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Замер #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  # переустанавливаем время последнего замера
except KeyboardInterrupt:
    # обработать исключение ctrl+c, чтобы предотвратить отображение его сообщений
    print('\nГотово.')
