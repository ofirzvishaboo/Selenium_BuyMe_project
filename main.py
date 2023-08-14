import pytest
from selenium.webdriver.chrome.service import Service
from RegisterPage import RegisterPage
from homescreen import HomeScreen
from sending_gifts import SendGifts
from PickBusiness import PickBusiness
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("/Users/ofir/mysh/seleniumchrome/chromedriver_mac_arm64/chromedriver"))
    yield driver
    driver.quit()

@pytest.fixture
def register_menu(driver):
    return RegisterPage(driver)

@pytest.fixture
def find_gift(driver):
    return HomeScreen(driver)

@pytest.fixture
def pick_business(driver):
    return PickBusiness(driver)

@pytest.fixture
def send_gifts(driver):
    return SendGifts(driver)

def test_registration(register_menu):
    register_menu.click_signup_button()
    register_menu.click_signup_text()
    # Fill details
    register_menu.enter_name()
    register_menu.enter_mail()
    register_menu.enter_password()
    register_menu.enter_password_confirmation()
    # Click checkbox and submit
    register_menu.click_login_checkbox()
    # register_menu.click_submit()
    # Assert name is correct
    register_menu.firstname_assertion()

def test_home_screen(find_gift):
    find_gift.sign_in()
    find_gift.select_price()
    find_gift.select_area()
    find_gift.select_category()
    find_gift.click_search()

def test_pick_business(pick_business):
    pick_business.assert_url()
    pick_business.click_business()
    pick_business.set_present_price()
    pick_business.click_choose()

def test_sending_gifts(send_gifts):
    send_gifts.receiver_name()
    # send_gifts.occasion()
    send_gifts.birthday_card("Mazal tov leha gever")
    # send_gifts.add_picture()
    send_gifts.click_continue()
    # send_gifts.click_now()
    send_gifts.choose_sms()
    send_gifts.gift_sender()
