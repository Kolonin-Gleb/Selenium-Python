import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Добавление расширения в настройки
options_chrome = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options_chrome.add_argument("--disable-search-engine-choice-screen")

# Указываем путь к профилю пользователя
options_chrome.add_argument(r'user-data-dir=C:\Users\glebk\AppData\Local\Google\Chrome\User Data')

# Инициализируем драйвер с указанными опциями
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://ya.ru/'
    browser.get(url)  # Открываем страницу
    time.sleep(5)  # Даем время на загрузку страницы
