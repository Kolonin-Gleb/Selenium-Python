# Работаем с браузером

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Чтобы не выбирать поисковый движок вручную
options = webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")

# Для грамотного закрытия браузера, даже при ошибке тестового сценария
with webdriver.Chrome(options=options) as driver:
    driver.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = driver.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)

