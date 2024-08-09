import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Добавление расширения в настройки
options_chrome = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options_chrome.add_argument("--disable-search-engine-choice-screen")

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless=chrome') # =chrome нужно указать до добавления расширений!
options_chrome.add_argument('--disable-gpu')

options_chrome.add_extension('4 options and args\coordinates.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)

    # Ищем элемент по тегу 'a' (ссылку)
    a = browser.find_element(By.TAG_NAME, 'a')
    
    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(a.get_attribute('href'))

    time.sleep(5)

