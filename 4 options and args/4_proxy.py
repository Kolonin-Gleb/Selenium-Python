# Работа с Proxy в Selenium проще чем в requests

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Добавление расширения в настройки
options_chrome = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options_chrome.add_argument("--disable-search-engine-choice-screen")

proxy = '8.210.83.33:80' # Для подмены IP используется proxy
# (Прокси можно покупать на время например тут: https://proxy6.net/?r=408871
# или тут https://proxy6.net/?r=408871)

# Использование Proxy
options_chrome.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://2ip.ru/'
    browser.get(url)
    time.sleep(5)
    # Получение своего ip с сайта
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)

# Расширение seleniumwire для работы Proxy с авторизацией

