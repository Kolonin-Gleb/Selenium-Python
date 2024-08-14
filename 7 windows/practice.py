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
"""

# 3 Перенос значений в Alert
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    time.sleep(2)
    spans = browser.find_elements(By.CLASS_NAME, 'pin')
    check = browser.find_element('id', 'check')

    for span in spans:
        pin = span.text
        check.click()
        window = browser.switch_to.alert
        window.send_keys(pin)
        window.accept()
        result = browser.find_element('id', 'result').text
        if result != '' and result != 'Неверный пин-код':
            print(result)
            break
"""

# 4 Настройки вьюпорта
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/window_size/1/')
    time.sleep(2)

    # Настройка размера окна (с учётом границ браузера)
    browser.set_window_size(555 + 16, 555 + 147) # Таким образом само окно отображения сайта будет 555*555
    time.sleep(100)
    # Получаю ответ
    result = browser.find_element('id', 'result').text
    print(result)
"""

# 5 Поиск секретного сочетания размера окна
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
with webdriver.Chrome(options=options) as driver:
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    driver.get('https://parsinger.ru/window_size/1/')
    time.sleep(2)

    # Автоматизированный расчёт пространства занимаемого рамками браузера
    inner_width = int(driver.find_element(By.ID, 'width').text.split(": ")[1])
    inner_height = int(driver.find_element(By.ID, 'height').text.split(": ")[1])
    outer_width = driver.get_window_size().get('width')
    outer_height = driver.get_window_size().get('height')

    target_width = outer_width - inner_width
    target_height = outer_height - inner_height

    for x in window_size_x:
        for y in window_size_y:
            driver.set_window_size(x + target_width, y + target_height)

            try:
                # Ожидание обновления текста в элементе result
                result = WebDriverWait(driver, 1).until(
                    EC.text_to_be_present_in_element((By.ID, 'result'), '')
                )
                result_text = driver.find_element(By.ID, 'result').text
                if result_text:
                    print(f"{x} x {y}")
                    print(result_text)
                    break
            except:
                # Если не обновилось в течение 1 секунды, продолжить
                continue
"""

# 7 Суммирование значений из title страниц
"""
with webdriver.Chrome(options=options) as browser:
    res_sum = 0
    browser.get('http://parsinger.ru/blank/3/index.html')
    [x.click() for x in browser.find_elements(By.CLASS_NAME, 'buttons')]
    tabs = browser.window_handles
    for tab in range(len(tabs)):
        browser.switch_to.window(browser.window_handles[tab])
        title = browser.execute_script("return document.title;")
        if title.isdigit():
            res_sum += (int(browser.execute_script("return document.title;")))
    print(res_sum)
"""

# 8 Суммирование корней из чисел на страницах
"""
with webdriver.Chrome(options=options) as browser:
    sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html']
    res_sum = 0

    for site in sites:
        browser.get(site)
        time.sleep(2)
        browser.find_element(By.TAG_NAME, 'input').click()
        res_sum += int(browser.find_element('id', 'result').text) ** 0.5

    print(round(res_sum, 9))
"""

# 9 Сбор и валидация значений из iframe-s
"""
from selenium.common import NoAlertPresentException
with webdriver.Chrome(options=options) as browser:
    browser.get("https://parsinger.ru/selenium/5.8/5/index.html")
    time.sleep(2)
    result_input = browser.find_element(By.CSS_SELECTOR, "#guessInput")
    result_check_button = browser.find_element(By.CSS_SELECTOR, "#checkBtn")

    # Проходка по iframes
    for iframe in browser.find_elements(By.CSS_SELECTOR, "iframe"):
        browser.switch_to.frame(iframe)
        browser.find_element(By.CSS_SELECTOR, "button").click()
        pin_code = browser.find_element(By.CSS_SELECTOR, "#numberDisplay").text
        # Возвращаемся в поле видимости основной страницы
        browser.switch_to.default_content()
        result_input.clear()
        result_input.send_keys(pin_code)
        result_check_button.click()
        try:
            print(browser.switch_to.alert.text)
        except NoAlertPresentException:
            continue
"""
