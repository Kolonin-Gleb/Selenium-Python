import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options.add_argument("--disable-search-engine-choice-screen")
# options.add_argument('--headless=new') # Без отрисовки интерфейса для оптимизации

# 1 Обновление страницы до получения нужного результата
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    code = browser.find_element(By.ID, 'result').text
    while code == 'refresh page':
        browser.refresh()
        code = browser.find_element(By.ID, 'result').text
        if code != 'refresh page':
            print(code)
"""

# 2 Чистка полей
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    elements = browser.find_elements(By.CLASS_NAME, 'text-field')
    for el in elements:
        el.clear()
    browser.find_element(By.ID, "checkButton").click()
    print(browser.switch_to.alert.text)
"""

# 3 Получение cookies по условию
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')

    cookies = browser.get_cookies()
    key_sum = 0
    for cookie in cookies:
        cookie_name_code = int(cookie['name'][cookie['name'].rfind("_")+1:])
        if cookie_name_code % 2 == 0:
            key_sum += int(cookie['value'])

    print(key_sum)
"""

# 4 Очистка полей по условию
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')

    boxes_el = browser.find_elements(By.CLASS_NAME, "text-field")
    for box_el in boxes_el:
        if box_el.get_attribute('disabled'):
            continue
        box_el.clear()
    
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
"""

# 5 Поиск cookie с самым долгим сроком жизни
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    links = []
    expires = []
    longest_expiry = 0
    longest_expiry_link = ''

    a_els = browser.find_elements(By.TAG_NAME, 'a')
    for a_el in a_els:
        links.append(a_el.get_attribute('href'))

    for link in links:
        browser.get(link)
        cookie = browser.get_cookie('foo2')
        # print(cookie['expiry'])
        if longest_expiry < int(cookie['expiry']):
            longest_expiry = cookie['expiry']
            longest_expiry_link = link

    print(longest_expiry)

    browser.get(longest_expiry_link)
    result = browser.find_element(By.ID, 'result').text
    print(result)
"""

# 6 Взаимодействие со скрытыми элементами
"""
with webdriver.Chrome(options=options) as browser:
    result_sum = 0
    browser.get('https://parsinger.ru/scroll/4/index.html')
    btn_els = browser.find_elements(By.CLASS_NAME, 'btn')
    for btn_el in btn_els:
        # Скролл сайта, чтобы нужный элемент оказался в поле видимости
        browser.execute_script("return arguments[0].scrollIntoView(true);", btn_el)
        btn_el.click()
        result_sum += int(browser.find_element(By.ID, 'result').text)

    print(result_sum)
"""

# 7 
"""
"""