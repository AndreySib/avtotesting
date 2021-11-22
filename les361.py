import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math

answer = math.log(int(time.time()))


#def test_exception1():
    #try: 
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(10)
    browser.quit()

@pytest.mark.parametrize('lesson', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
def test_lesson_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1/"
    browser.get(link)
            #browser = webdriver.Chrome()
            #browser.get("https://stepik.org/lesson/{lesson}/step/1")
        
            # Говорим браузеру ждать 15 сек пока поле для ввода не загрузится на странице
    input1 = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea")))
    input1 = browser.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea")
        
            # отправляем ответ из формулы вверху в поле для ввода
    input1.send_keys(str(answer))
        
            # Говорим браузеру ждать 25 секунд по кнопка Отправить не станет кликабельной
    button1 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember73 > div > section > div > div.attempt__inner > div.attempt__actions > button")))
    button1 = browser.find_element_by_css_selector ("#ember73 > div > section > div > div.attempt__inner > div.attempt__actions > button")
            # кликаем на кнопку
    button1.click()
    tex = WebDriverWait(browser, 25).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div[1]/div[2]/div/pre'), 'Correct!'))
            #pytest.fail('Текст не соответсвует - Correct!')

#@pytest.mark.xfail(reason="fixing this bug right now")
#def test_text_correct():
            #browser.text_to_be_present_in_element_value(('#ember91 > pre'), 'Correct!')
                

            # Добавляем тест на соответсвие текста в поле после всех манипуляций 
#@pytest.mark.xfail
#def test_text_correct2():
            #cor2 = browser.text_to_be_present_in_element_value(('#ember91 > pre'), 'Correct!')
            #pytest.fail('Текст не соответсвует - Correct!')
                
                #with pytest.raises(NoSuchElementException):
                
    

    #button = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#ember91 > pre'), 'Correct!'))



    #finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
                #time.sleep(20)
            # закрываем браузер после всех манипуляций
                #browser.quit()
