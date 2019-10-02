import pytest

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()


@pytest.mark.parametrize("language", ["ru", "en-gb"])
class TestLogin:
    def test_quest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
