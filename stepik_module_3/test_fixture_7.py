import pytest


@pytest.mark.parametrize("language", ["ru", "en-gb"])
class TestLogin:
    def test_quest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
