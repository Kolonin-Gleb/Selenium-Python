# Неявные ожидания
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# Импорт ожиданий
from selenium.webdriver.support import expected_conditions as EC # метод
from selenium.webdriver.support.ui import WebDriverWait # Класс

options = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options.add_argument("--disable-search-engine-choice-screen")


# 1 Пример неявного ожидания
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('http://parsinger.ru/expectations/1/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    time.sleep(3)
    print(browser.find_element(By.ID, 'result').text)
"""

# Глобальная настройка ожидания появления элементов

"""
"""


