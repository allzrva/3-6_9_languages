# run this test with command pytest --language=es test_items.py
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_displayed(browser):
    browser.get(link)
    # if no such elements found, an empty list is returned. Empty list evaluates as False.
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), \
        "'Add to cart' button should be displayed on the web page."
