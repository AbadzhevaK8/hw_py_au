#! python
# downloadXkcd.py - Загружает все комиксы xkcd.

import requests, os, bs4

url = 'http://xkcd.com' # начальный url-адрес
os.makedirs('xkcd', exist_ok=True) # сохраняем комикс в папке ./xkcd

while not url.endwith('#'):
    # Загрузка страницы.
    print('Загружается страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Поиск url-адреса изображения комикса.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображение комикса.')
    else:

print('Готово.')
