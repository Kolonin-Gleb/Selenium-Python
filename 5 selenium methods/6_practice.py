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

# 7 Получить значения из полей при checked checkboxes
"""
with webdriver.Chrome(options=options) as browser:
    result_sum = 0
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')

    textareas_els = browser.find_elements(By.TAG_NAME, 'textarea')
    checkboxes_els = browser.find_elements(By.TAG_NAME, 'input')

    for textarea_el, checkbox_el in zip(textareas_els, checkboxes_els):
        if checkbox_el.is_selected() == True:
            result_sum += int(textarea_el.text)

    print(result_sum)
"""

# 8 Перенос значений и выполнение проверок
"""
with webdriver.Chrome(options=options) as browser:
    browser.get("https://parsinger.ru/selenium/5.5/4/1.html")

    buttons_els = browser.find_elements(By.TAG_NAME, 'button')

    # Собираю все значения из grey boxes и стираю их
    grey_boxes_values = []
    for i in range(1, 51):
        grey_box = browser.find_element(By.XPATH, f'//*[@id="container"]/div[{i}]/textarea[1]')
        grey_boxes_values.append(grey_box.text)
        grey_box.clear()
    
    # Устанавливаю значения в blue boxes и выполняю проверку
    for i in range(1, 51):
        # Установка значений
        browser.find_element(By.XPATH, f'//*[@id="container"]/div[{i}]/textarea[2]').send_keys(grey_boxes_values[i-1])
        # Проверка (перекраска полей)
        buttons_els[i-1].click()

    buttons_els[-1].click() # Итоговая кнопка проверки
    time.sleep(10)
"""

# 9 Работа с кнопками, выпадающими списками, checkbox-ами
"""
from selenium.webdriver.support.ui import Select
with webdriver.Chrome(options=options) as browser:
    browser.get("https://parsinger.ru/selenium/5.5/5/1.html") # task link
    time.sleep(2) # чтобы страница точно успела загрузиться
    
    color_codes = []
    span_els = browser.find_elements(By.TAG_NAME, 'span') # color codes elements
    color_codes = [span_el.text for span_el in span_els]

    select_els = browser.find_elements(By.TAG_NAME, 'select') # drop-down lists
    input_els = browser.find_elements(By.TAG_NAME, 'input') # input fileds

    # Получение div-ов с цветнымми кнопками
    div_buttons_els = []
    for i in range(1, 51): # TODO: Магическое число. Известно, что на сайте имеется 50 блоков с кнопками
        div_buttons_els.append(browser.find_element(By.XPATH, f'//*[@id="main-container"]/div[{i}]/div'))

    # простановка checkboxes и вставка цветов в input
    color_codes_iterator = iter(color_codes) # TODO: можно ли написать оптимальнее?
    for i, input_el in enumerate(input_els):
        if i % 2 == 0:
            input_el.click()
        else:
            input_el.send_keys(next(color_codes_iterator))

    # Установка цвета в выпадающие списки и нажатие кнопок того же цвета
    for div_button_el, color, select_el in zip(div_buttons_els, color_codes, select_els):
        # Установка цвета в вып. список
        select_el = Select(select_el)
        select_el.select_by_value(color)
        # Нажатие кнопки того же цвета
        buttons_els = div_button_el.find_elements(By.TAG_NAME, 'button')
        for button_el in buttons_els:
            if button_el.get_attribute('data-hex') == color:
                button_el.click() # нажите кнопки цвета
                break

    # Проверка всех секций
    for i in range(1, 51): # TODO: Магическое число. Известно, что на сайте имеется 50 блоков с кнопками
        browser.find_element(By.XPATH, f'//*[@id="main-container"]/div[{i}]/button').click()

    # Руками нажимаю последнюю кнопку
    time.sleep(30)
"""

# 10 
"""
"""



