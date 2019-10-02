import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def calc_sum(a, b):
    return a + b


test_page = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(test_page)

try:
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    res = calc_sum(num1, num2)
    Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(res))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
