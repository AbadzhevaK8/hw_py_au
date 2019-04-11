#! python3
# multidownloadXkcd.py - загружает комиксы в несколько потоков.

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)  # сохраняем комиксы в папке xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # загрузка страницы
        print('Загрузка страницы https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Поиск url-адреса изображения комикса.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Не удается найти изображение комикса.')
        else:
            try:
                comicUrl = 'http:' + comicElem[0].get('src')
                # Загрузка изображения.
                print('Загрузка изображения %s...' % comicUrl)
                res = requests.get(comicUrl)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                print('Missing schema.')
                # пропустить комикс
                continue

                """
                comicUrl = comicElem[0].get('src')
                # Загрузка изображения
                print('Загрузка изображения %s...' % comicUrl)
                res = requests.get(comicUrl)
                res.raise_for_status()
                """

            # Сохранение изображения в папке ./xkcd
            imageFile = open(os.path.join(
                'xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# создание и запуск объектов thread
downloadThreads = []  # список всех объектов thread
for i in range(0, 1400, 100):  # 14 итераций, создающих 14 потоков
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# ожидание завершения всех потоков
for downloadThread in downloadThreads:
    downloadThread.join()
print('Готово.')
