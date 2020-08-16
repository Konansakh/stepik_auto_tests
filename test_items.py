import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_cart(browser):
    browser.get(link)
    basket_button = browser.find_element_by_class_name("btn-add-to-basket")
    basket_attribute = basket_button.get_attribute("value")
    print("value of basket_attrubite: ", basket_attribute)
    assert basket_attribute is not None, "Not found basket attribute (possible button not found, please check it"
    time.sleep(30)
