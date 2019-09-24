import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from py_selenium.lesson2_1_step4 import calc


test_page = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(test_page)

try:
    value = browser.find_element(By.ID, "input_value").text
    res = calc(value)
    browser.find_element(By.ID, "answer").send_keys(res)
    robot_check_box = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check_box)
    robot_check_box.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
