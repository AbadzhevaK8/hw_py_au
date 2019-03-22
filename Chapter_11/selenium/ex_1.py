#! python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Найден элемент <%s> с данным именем класса!' % (elem.tag_name))
except:
    print('Не удалось найти элемент с данным именем класса.')
