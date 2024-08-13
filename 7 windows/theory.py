import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# Чтобы не выбирать поисковый движок вручную
options.add_argument("--disable-search-engine-choice-screen")

# ============================= 1 Вкладки в браузере
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
    print(browser.window_handles)
    time.sleep(10)
"""

# Пример итерации по вкладкам
"""
with webdriver.Chrome(options=options) as browser:
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')

    for x in range(len(browser.window_handles)): # итерация в хаотичном порядке!?
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        print(browser.execute_script("return document.title;"), browser.window_handles[x])
"""

# ============================= 2 Размеры окна
"""
with webdriver.Chrome(options=options) as browser:
    browser.get('http://parsinger.ru/window_size/1/')
    browser.set_window_size(1200, 720)
    time.sleep(5)
"""

# ============================= 3 Модальные окна (Alert, Prompt, Confirm)
"""
# Пример с окном Prompt
with webdriver.Chrome(options=options) as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'prompt').click() # Вызыв окна
    time.sleep(2)
    prompt = browser.switch_to.alert # Переход в окно (делаем его активным)
    prompt.send_keys('Введёный текст')
    # prompt.accept() # Подтвержаем отправку текста
    prompt.dismiss() # Отмена отправки Prompt
    time.sleep(.5)
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)
"""

# ============================= 4 Работа с фреймами
"""
# Чтобы выйти из iFrame или frameset, вернитесь к содержимому по умолчанию.
# driver.switch_to.default_content()

# Получение информации из iframe
with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.8/4/index.html')
    time.sleep(2)

    # Переключаемся на iframe
    iframe_element = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe_element)

    # Получение исходного HTML ВСЕЙ СТРАНИЦЫ? ПОЧЕМУ НЕ iframe?
    iframe_content = browser.page_source
    print(iframe_content)
"""


