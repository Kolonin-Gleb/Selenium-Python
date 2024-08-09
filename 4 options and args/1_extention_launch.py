import time
from selenium import webdriver

# Добавление расширения в настройки
options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('4 options and args\coordinates.crx')
# Чтобы не выбирать поисковый движок вручную
options_chrome.add_argument("--disable-search-engine-choice-screen")

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)


"""
Некоторые популярные расширения.
AdBlock / uBlock Origin: для блокировки рекламы.

EditThisCookie: для работы с куками.
User-Agent Switcher: для смены User-Agent.
Firebug / Chrome Developer Tools: для отладки и анализа.
Screenshot: для скриншотов и записи экрана.
LastPass / 1Password: для автоматического заполнения форм, если это нужно в тестах.
Proxy SwitchyOmega: для работы с прокси-серверами.
Wappalyzer: для определения технологий, используемых на веб-сайте.
Tampermonkey: Для запуска пользовательских скриптов, что может быть полезно
для автоматизации сложных действий на веб-странице.
"""

