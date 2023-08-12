from unittest import TestCase
from selenium.webdriver.chrome.service import Service
from login import LoginPage
from homescreen import HomeScreen
from selenium import webdriver

class TestBuyMe(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("/Users/ofir/mysh/seleniumchrome/chromedriver_mac_arm64/chromedriver"))
        self.driver.get('https://buyme.co.il/')
        self.register_menu = LoginPage(self.driver)
        self.find_gift = HomeScreen(self.driver)
        # implicit wait
        self.driver.implicitly_wait(10)
        # page load timeout
        self.driver.set_page_load_timeout(10)

    def test_registration(self):
        self.register_menu.click_signup_button()
        self.register_menu.click_signup_text()
        self.register_menu.enter_name()
        self.register_menu.enter_mail()
        self.register_menu.enter_password()
        self.register_menu.enter_password_confirmation()
        self.register_menu.click_login_checkbox()
        self.register_menu.click_submit()
        self.register_menu.firstname_assertion()

    def home_screen(self):
        self.find_gift.select_price()
        self.find_gift.select_area()
        self.find_gift.select_category()
        self.find_gift.click_search()
        self.find_gift.assert_url()
        self.find_gift.click_business()
        self.find_gift.set_present_price()
        self.find_gift.click_choose()
        self.find_gift.receiver_name()
        self.find_gift.occasion()
        self.find_gift.birthday_card("Mazal tov leha gever")
        self.find_gift.add_picture()
        self.find_gift.click_continue()
        self.find_gift.click_now()
        self.find_gift.choose_sms()
        self.find_gift.gift_sender()

    def tearDown(self):
        self.driver.quit()

