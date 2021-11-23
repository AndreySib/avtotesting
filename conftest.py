import pytest
from selenium import webdriver
#Это фикстура, своего рода правило работы функции browser, дальше в других файлах можно просто написать ссылку куда переходить и не обязательно прописывать это в каждом файле тоже самое можно и с другими функциями.
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()