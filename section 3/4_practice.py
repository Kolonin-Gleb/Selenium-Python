import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Чтобы не выбирать поисковый движок вручную
options = webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")

# Скрипт 1. Заполнение формы за 3 секунды
"""
url = 'http://parsinger.ru/selenium/1/1.html'

with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    for field in browser.find_elements(By.CLASS_NAME, 'form'):
        field.send_keys('Text')
    browser.find_element(By.ID, 'btn').click()
    print(browser.find_element(By.ID,'result').text)
"""

# Скрипт 2. 
"""
"""



