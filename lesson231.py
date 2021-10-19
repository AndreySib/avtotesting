from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # нажимаем кнопку
    button = browser.find_element_by_css_selector ("button.trollface")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    #переключаемся на новую вкладку виндоус
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


# берем число из Х подставляем в формулу на верху
    x = browser.find_element_by_id ('input_value')
    #x = x.get_attribute("input_value")
    x = x.text
    y = calc(x)
    
    # вставляем число в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()