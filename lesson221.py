from selenium import webdriver
import time

#код который считает формулу
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element_by_id ('input_value')
	#x = x.get_attribute("input_value")
	x = x.text
	y = calc(x)

	
	# код, который заполняет обязательные поля
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
	option1 = browser.find_element_by_id("robotCheckbox")
	option1.click()
	
	option2 = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
	option2.click()
	#option2 = browser.find_element_by_id("robotsRule")
	
	

	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()