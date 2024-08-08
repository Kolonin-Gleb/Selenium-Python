# Поиск элементов Selenium
# Локатор - способ идентификации эл. на странице (аргумент)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Чтобы не выбирать поисковый движок вручную
options = webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")
browser = webdriver.Chrome(options=options)


# Пример поиска. find_element()
'''
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, "sale_button").click()

time.sleep(10)
'''

# Результат поиска - объект WebElement формата DOM-дерева страницы, где осуществляется поиск 

url = 'http://parsinger.ru/selenium/3/3.html'
browser.get(url)
elem = browser.find_element(By.CLASS_NAME, 'text')
print(elem)

time.sleep(7)
browser.quit()

