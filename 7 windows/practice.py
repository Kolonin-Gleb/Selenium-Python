import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options.add_argument("--disable-search-engine-choice-screen")

# 1 Переключение между Alert окнами для поиска ответа
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    time.sleep(2)

    input_els = browser.find_elements(By.TAG_NAME, 'input')

    for input_el in input_els:
        input_el.click()
        window = browser.switch_to.alert
        window.accept()
        if browser.find_element(By.ID, 'result').text != '':
            print(browser.find_element(By.ID, 'result').text)
            break
    
    time.sleep(100)
"""

# 2 Получение кодов из Alert и их валидация
"""
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    time.sleep(2)

    input_els = browser.find_elements(By.CLASS_NAME, 'buttons')
    validation_input_el = browser.find_element(By.ID, 'input')
    check_input_el = browser.find_element(By.ID, 'check')
    p_result_el = browser.find_element(By.ID, 'result')

    for input_el in input_els:
        input_el.click()
        window = browser.switch_to.alert
        window_text = window.text
        window.accept()

        # Валидация
        validation_input_el.send_keys(window_text)
        check_input_el.click()
        

        if p_result_el.text != '' and p_result_el.text != 'Неверный пин-код':
            print(p_result_el.text)
            break
        
    time.sleep(100)

