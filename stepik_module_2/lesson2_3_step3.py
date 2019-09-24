import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from py_selenium.lesson2_1_step4 import calc


test_page = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(test_page)

try:
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()
    value = browser.find_element(By.ID, "input_value").text
    res = calc(value)
    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()




