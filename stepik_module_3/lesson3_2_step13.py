import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistrationPage(unittest.TestCase):
    """
    Тест страниц регистрации
    """

    def test_first_registration_page(self):
        """Тест страницы регистрации 1"""

        self.url = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.get(self.url)

        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("test@email.com")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        self.actual_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(self.actual_text, self.expected_text, "Actual text does not match expected")
        self.browser.quit()

    def test_second_registration_page(self):
        """Тест страницы регистрации 2"""

        self.url = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.get(self.url)

        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("test@email.com")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        self.actual_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(self.actual_text, self.expected_text, "Actual text does not match expected")
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
