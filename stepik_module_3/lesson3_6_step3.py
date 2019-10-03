import time
import math

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_answer():
    answer = math.log(int(time.time()))
    return str(answer)


lessons = ["236895", "236896", "236897", "236898",
           "236899", "236903", "236904", "236905"]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser...")
    browser.quit()


@pytest.mark.parametrize("lesson", lessons)
def test_parametrize_url(browser, lesson):
    browser.get(f"https://stepik.org/lesson/{lesson}/step/1")
    browser.find_element(By.CLASS_NAME, "textarea").send_keys(get_answer())
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    text = browser.find_element(By.CSS_SELECTOR, "div>pre").text
    assert text == "Correct!", f"expected result: 'Correct!', actual result: {text}"
