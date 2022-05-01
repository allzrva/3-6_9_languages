# run this test with command pytest --language=es test_items.py
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_displayed(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button, "'Add to cart' button should be displayed on the web page."
