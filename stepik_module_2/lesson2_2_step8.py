import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")
test_page = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(test_page)

try:
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Smith")
    browser.find_element(By.NAME, "email").send_keys("test@email.ru")
    browser.find_element(By.NAME, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
