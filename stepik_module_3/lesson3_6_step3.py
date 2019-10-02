import pytest
import time
import math

from selenium import webdriver


def get_answer():
    answer = math.log(int(time.time()))
    return answer


link = ["236895"]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait()
    yield browser
    print("\nquit browser")
    browser.quit()


@pytest.mark.parametrize("page", link)
def test_input_correct_answer(browser, page):
    test_page = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(test_page)
    browser.find_element_by_css_selector(".textarea").send_keys(get_answer())
    time.sleep(3)
