import pytest
from selenium.webdriver.chrome.service import Service
from RegisterPage import RegisterPage
from HomeScreen import HomeScreen
from SendGifts import SendGifts
from PickBusiness import PickBusiness
from selenium import webdriver
import json

with open('config.json') as file:
    data = json.load(file)


@pytest.fixture
def driver():
    if data["browser"] == 'chrome':
        driver = webdriver.Chrome(service=Service("/Users/ofirzvishaboo/Documents/chromedriver-mac-arm64/chromedriver"))
    elif data["browser"] == 'firefox':
        driver = webdriver.Firefox(service=Service("/Users/ofirzvishaboo/Documents/chromedriver-mac-arm64/chromedriver"))
    driver.get(data["url"])
    yield driver
    driver.quit()


def test_all(driver):
    register_menu = RegisterPage(driver)
    register_menu.click_signup_button()
    register_menu.click_signup_text()
    # Fill details
    register_menu.enter_name()
    register_menu.enter_mail()
    register_menu.enter_password()
    register_menu.enter_password_confirmation()
    # Click checkbox and submit
    register_menu.click_login_checkbox()
    register_menu.click_submit()
    # Assert name is correct
    register_menu.get_screenshot()
    register_menu.firstname_assertion()

    find_gift = HomeScreen(driver)
    # find_gift.sign_in()
    find_gift.select_price()
    find_gift.select_area()
    find_gift.select_category()
    find_gift.click_search()

    pick_business = PickBusiness(driver)
    pick_business.assert_url()
    pick_business.click_business()
    pick_business.set_present_price()
    pick_business.click_choose()

    send_gifts = SendGifts(driver)
    send_gifts.receiver_name()
    send_gifts.occasion()
    send_gifts.birthday_card("Mazal tov leha gever")
    send_gifts.add_picture()
    send_gifts.click_continue()
    send_gifts.choose_sms()
    send_gifts.gift_sender()
