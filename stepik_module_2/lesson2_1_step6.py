import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from py_selenium.lesson2_1_step4 import calc


test_page = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(test_page)

try:
    value_x = browser.find_element(By.ID, "treasure").get_attribute('valuex')
    result = calc(value_x)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
