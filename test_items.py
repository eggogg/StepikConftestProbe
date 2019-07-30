link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_should_be_on_the_page(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
