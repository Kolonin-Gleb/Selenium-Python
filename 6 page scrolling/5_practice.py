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

# 2 Сбор чисел с бесконечной ленты.
# Я собрал данные с помощью выделения.
# Сложил 5ти значные числа в Excel и прибавил к ним сумму 6ти значных, полученных из этой стрки при копировании.
# def split_text(text, chunk_size=6):
#     return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
# # Пример использования
# stochka = '910510911511912512913513914514915515916516917517918518919519920520921521923523924524922522926526925525927527928528931531929529930530932532933533934534935535936536937537938538939539940540941541942542943543945545946546944544950550947547948548949549951551956556957557953553954554955555952552958558959559960560961561963563964564962562966566967567965565968568970570971571969569972572973573974574975575976576978578979579982582977577980580981581983583984584985585986586990590991591987587988588989589992592995595993593994594999599998598996596997597'
# result = split_text(stochka)
# result = [int(num) for num in result]
# print(sum(result))


# 2 Сбор чисел с бесконечной ленты.
# Программное решение
"""
"""

