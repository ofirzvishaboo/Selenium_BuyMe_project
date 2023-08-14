
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
    # find_gift.select_price()
    # find_gift.select_area()
    # find_gift.select_category()
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

# class TestBuyMe(TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(service=Service("/Users/ofir/mysh/seleniumchrome/chromedriver_mac_arm64/chromedriver"))
#         self.driver.get('https://buyme.co.il/')
#         self.register_menu = LoginPage(self.driver)
#         self.find_gift = HomeScreen(self.driver)
#         self.pick_business = PickBusiness(self.driver)
#         self.send_gifts = SendGifts(self.driver)
#         # implicit wait
#         self.driver.implicitly_wait(10)
#         # page load timeout
#         self.driver.set_page_load_timeout(10)
#
#     def test_registration(self):
#         self.register_menu.click_signup_button()
#         self.register_menu.click_signup_text()
#         # Fill details
#         self.register_menu.enter_name()
#         self.register_menu.enter_mail()
#         self.register_menu.enter_password()
#         self.register_menu.enter_password_confirmation()
#         # Click checkbox and submit
#         self.register_menu.click_login_checkbox()
#         self.register_menu.click_submit()
#         # Assert name is correct
#         self.register_menu.firstname_assertion()
#
#     def test_home_screen(self):
#         # self.find_gift.sign_in()
#         self.find_gift.select_price()
#         self.find_gift.select_area()
#         self.find_gift.select_category()
#         self.find_gift.click_search()
#
#     def test_pick_business(self):
#         self.pick_business.assert_url()
#         self.pick_business.click_business()
#         self.pick_business.set_present_price()
#         self.pick_business.click_choose()
#
#     def test_sending_gifts(self):
#         self.send_gifts.receiver_name()
#         # self.send_gifts.occasion()
#         self.send_gifts.birthday_card("Mazal tov leha gever")
#         # self.send_gifts.add_picture()
#         self.send_gifts.click_continue()
#         # self.send_gifts.click_now()
#         self.send_gifts.choose_sms()
#         self.send_gifts.gift_sender()
#
#     def tearDown(self):
#         self.driver.quit()
