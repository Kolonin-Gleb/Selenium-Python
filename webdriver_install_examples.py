# Автоматическая и Ручная Установка Selenium и WebDriver

# 1) pip install selenium
# Очень полезный функционал, чтобы не возиться с установкой!!!
# 2) pip install webdriver_manager

# Автоматическая установка
'''
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Будет установлен драйвер для взаимодействия с тек. версией Chrome
with webdriver.Chrome(ChromeDriverManager().install()) as driver:
    # TODO: Как установить выбор поискового движка при автоматической установке?
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=options)
    driver.get("https://stepik.org/course/104774")
    time.sleep(5)
'''

# Ручная установка
# https://stepik.org/lesson/730646/step/2?unit=732177
# Код для теста
'''
import time
from selenium import webdriver

url = 'https://stepik.org/course/104774'

# Чтобы не выбирать поисковый движок вручную
options = webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(10)
'''














