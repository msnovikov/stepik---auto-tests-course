from selenium import webdriver
from selenium.webdriver.common.by import By


test_page = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()
# задаем неявное ожидание для поиска элементов
browser.implicitly_wait(5)
browser.get(test_page)

try:
    browser.find_element(By.ID, "verify").click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
finally:
    browser.quit()
