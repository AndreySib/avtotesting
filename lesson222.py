from selenium import webdriver
import time
import os 

try: 
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element_by_name ('firstname')
	y = browser.find_element_by_name ('lastname')
	z = browser.find_element_by_css_selector ('body > div > form > div > input:nth-child(6)')

	x.send_keys("A")
	y.send_keys("B")
	z.send_keys("C")

	current_dir = os.path.abspath(os.path.dirname(__file__))    
	# получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'file.txt')           
	# добавляем к этому пути имя файла 
	# находим кнопку загрузить файл 
	element = browser.find_element_by_css_selector ('input#file')
	# отправляем полученный путь скачивания файла
	element.send_keys(file_path)

	button = browser.find_element_by_tag_name("button")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
