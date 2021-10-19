from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
        browser = webdriver.Chrome()

        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        
        button1 = browser.find_element_by_css_selector ("button#book")
        button1 = WebDriverWait(browser, 16).until(
        EC.element_to_be_clickable((By.ID, "book")))
        #button.click()
        #message = browser.find_element_by_id("book")
        
        #assert "successful" in message.text
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        button = WebDriverWait(browser, 22).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
        
        #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button1.click()
        #assert "successful" in message.text
       # нажимаем кнопку
        #button2 = browser.find_element_by_css_selector ("button#solve")
        #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        #button2.click()
# берем число из Х подставляем в формулу на верху
        x = browser.find_element_by_id ('input_value')
    #x = x.get_attribute("input_value")
        x = x.text
        y = calc(x)
    
    # вставляем число в поле
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)

        button2 = browser.find_element_by_css_selector ("button#solve")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button2.click()



finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(20)
        # закрываем браузер после всех манипуляций
        browser.quit()