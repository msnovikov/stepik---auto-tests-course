"""
Для проверки работы необходимо раскоментировать
строку с импортом модуля time
и строку с вызовом метода sleep
"""
# import time

from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_the_basket_button_is_on_the_page(browser):
    browser.get(link)
    # time.sleep(30)
    # находим кнопку с классом btn-add-to-basket на странице
    button_list = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    # проверяем, что длина списка не равна 0, т.е кнопка найдена
    assert len(button_list) != 0, f"button not found on page {link}"
