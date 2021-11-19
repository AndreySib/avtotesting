import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

def test_exception1():
    try: 
            browser = webdriver.Chrome()
            browser.get("https://stepik.org/lesson/236895/step/1")
        
            # Говорим браузеру ждать 15 сек пока поле для ввода не загрузится на странице
            input1 = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
            input1 = browser.find_element_by_css_selector("#ember85")
        
            # отправляем ответ из формулы вверху в поле для ввода
            input1.send_keys(str(answer))
        
            # Говорим браузеру ждать 25 секунд по кнопка Отправить не станет кликабельной
            button1 = WebDriverWait(browser, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember73 > div > section > div > div.attempt__inner > div.attempt__actions > button")))
            button1 = browser.find_element_by_css_selector ("#ember73 > div > section > div > div.attempt__inner > div.attempt__actions > button")
            # кликаем на кнопку
            button1.click()
            
            # Добавляем тест на соответсвие текста в поле после всех манипуляций 
            with pytest.raises(NoSuchText):
                browser.find_element_by_css_selector('#ember91 > pre'), 'Correct!'
                pytest.fail('Текст не соответсвует - Correct!')

            #button = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#ember91 > pre'), 'Correct!'))


    finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(20)
            # закрываем браузер после всех манипуляций
            browser.quit()

