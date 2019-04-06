#! python3
# quickWeather.py - выводит прогноз погоды для заданного населенного пункта.

import json, requests, sys

# определение названия населенного пункта из аргументов командной строки.
if len(sys.argv) < 2:
    print('Использование: quickWeather.py местоположение')
    sys.exit()
location = ' '.join(sys.argv[1:])

# загружаем json-данные из api сайта openweathermap.org.
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=a4c0639c9f32776a6b3816e0ffa34d26' % (location)
response = requests.get(url)
response.raise_for_status()

# загрузка json-данных в переменную python.
weatherData = json.loads(response.text)
# вывод прогноза погоды
w = weatherData['list']
print('Погода сегодня в %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Завтра:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Послезавтра:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
