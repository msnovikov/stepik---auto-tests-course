import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


test_page = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(test_page)

try:
    value = browser.find_element(By.ID, "input_value").text
    result = calc(value)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
