import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options.add_argument("--disable-search-engine-choice-screen")

# 1 sum of spans
"""
with webdriver.Chrome(options=options) as browser:
    result_sum = 0
    browser.get('https://parsinger.ru/scroll/2/index.html')
    input_els = browser.find_elements(By.TAG_NAME, 'input')
    for input_el in input_els:
        input_el.click()

    span_els = browser.find_elements(By.TAG_NAME, 'span')
    for span_el in span_els:
        if span_el.text != '':
            result_sum += int(span_el.text)

    print(result_sum)
"""

# 1 sum of spans using scrolling
"""
from selenium.webdriver import Keys
with webdriver.Chrome(options=options) as browser:
    browser.get('http://parsinger.ru/scroll/2/')
    result_sum = 0
    
    for tag_input in browser.find_elements(By.TAG_NAME, 'input'):
        tag_input.send_keys(Keys.TAB) # Для перемещения к следующему элементу
        tag_input.click()

    for x in browser.find_elements(By.TAG_NAME, 'span'):
        if x.text.isdigit():
            result_sum += int(x.text)

    print(result_sum)
"""

# 2 Сбор и суммирование чисел с бесконечной ленты.
# Я собрал данные с помощью выделения.
# Сложил 5ти значные числа в Excel и прибавил к ним сумму 6ти значных, полученных из этой стрки при копировании.
# def split_text(text, chunk_size=6):
#     return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
# # Пример использования
# stochka = '910510911511912512913513914514915515916516917517918518919519920520921521923523924524922522926526925525927527928528931531929529930530932532933533934534935535936536937537938538939539940540941541942542943543945545946546944544950550947547948548949549951551956556957557953553954554955555952552958558959559960560961561963563964564962562966566967567965565968568970570971571969569972572973573974574975575976576978578979579982582977577980580981581983583984584985585986586990590991591987587988588989589992592995595993593994594999599998598996596997597'
# result = split_text(stochka)
# result = [int(num) for num in result]
# print(sum(result))


# 2 Сбор и суммирование чисел с бесконечной ленты.
# Программное решение
"""
from selenium.webdriver.common.action_chains import ActionChains
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(3)
    result_sum = 0
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div') # Первый div вложенный в div контейнер

    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 10).perform()
        time.sleep(2)

    elements = browser.find_elements(By.XPATH, '//span[starts-with(@id, "__InfiScroll_")]')

    for element in elements:
        value = element.text
        if value.isdigit():
            result_sum += int(value)

    print(result_sum)
"""

# 3 Сбор и суммирование чисел с бесконечной ленты.
"""
from selenium.webdriver.common.action_chains import ActionChains
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    time.sleep(3)
    result_sum = 0
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div') # Первый div вложенный в div контейнер

    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 10).perform()
        time.sleep(1)

    elements = browser.find_elements(By.XPATH, '//p[starts-with(@id, "__InfiScroll_")]')

    for element in elements:
        value = element.text
        if value.isdigit():
            result_sum += int(value)

    print(result_sum)
"""

# 4 Сбор и суммирование чисел из нескольких окон прокрутки.
"""
from selenium.webdriver.common.action_chains import ActionChains
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    time.sleep(2)
    result_sum = 0

    for i in range(1, 6):
        div = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]/div')

        for x in range(10):
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 10).perform()
            time.sleep(1)
        ActionChains(browser).reset_actions()

    # Находит сразу все прогруженные ранее значения во всех скроллах
    elements = browser.find_elements(By.XPATH, '//span[starts-with(@id, "__InfiScroll_")]')

    for element in elements:
        result_sum += int(element.text)

    print(result_sum) # 443968780 # 159858750
"""

# 5 Клики по элементам
"""
# При использовании selenium 4.21.0, клики по элементам работают без нужды в скролле к элементу.
# Так ли это?
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    time.sleep(2)
    uran_els = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for uran_el in uran_els:
        uran_el.click()
    
    time.sleep(1000)
"""

# Answer: GFL4-ED40-F32F-HJ24-0BXS-235N-PIRE-123VD-123F
# 6 Удерживание кнопок нужное время
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
with webdriver.Chrome(options=options) as driver:
    driver.get('https://parsinger.ru/selenium/5.7/5/index.html')
    buttons = driver.find_elements(By.XPATH, "//button[@class='timer_button']")
    for button in buttons:
        hold_time = float(button.text)
        action = ActionChains(driver)
        action.click_and_hold(button).pause(hold_time).release(button).perform()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = driver.switch_to.alert.text
    print(alert_text)
"""

# 7 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome(options=options) as browser:
    browser.get("https://parsinger.ru/selenium/5.7/4/index.html")

    while len(browser.find_elements(By.CSS_SELECTOR, "input")) < 1000: # Пока не находим все input-ы
        # находим последний на этой странице и скролим до него.
        last = browser.find_element(By.CSS_SELECTOR, ".child_container:last-child")
        browser.execute_script("return arguments[0].scrollIntoView(true)", last)

    # Обработка всех прогруженных input-ов
    for cb in browser.find_elements(By.CSS_SELECTOR, "input"):
        if int(cb.get_attribute("value")) % 2 == 0:
            # Скролим до тех input, что чётные и требуют нажатия
            browser.execute_script("return arguments[0].scrollIntoView(true)", cb)
            cb.click()
    
    browser.find_element(By.CSS_SELECTOR, ".alert_button").click()
    print(browser.switch_to.alert.text) # 5402f04236450f263540jk406504l506
"""


    