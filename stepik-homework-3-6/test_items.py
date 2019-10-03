import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_the_basket_button_is_on_the_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")
# TODO доделать assert и отправить на ревью
