from selenium.webdriver.common.by import By
from BasePage import BasePage

class SendGifts(BasePage):
    SELECTORS = {
        "RECEIVER_NAME_INPUT": (By.CSS_SELECTOR, "input[title='שם מקבל המתנה']"),
        "OCCASION_SELECT": (By.CSS_SELECTOR, "select[name='eventType']"),
        "BIRTHDAY_CARD_TEXTAREA": (By.CSS_SELECTOR, "textarea[data-parsley-group='voucher-greeting']"),
        "CONTINUE_BUTTON": (By.CSS_SELECTOR, "button[gtm='המשך']"),
        "CHOOSE_SMS_SVG": (By.CSS_SELECTOR, "svg[gtm='method-sms']"),
        "SMS_INPUT": (By.CSS_SELECTOR, "input[id=sms]"),
        "GIFT_SENDER_INPUT": (By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']"),
        "CLICK_NOW_DIV": (By.CSS_SELECTOR, "div[gtm='עכשיו']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"
        self.driver.get("https://buyme.co.il/money/752649?price=300")

    def receiver_name(self):
        self.enter_text(*self.SELECTORS["RECEIVER_NAME_INPUT"], "ohad")

    def occasion(self):
        self.select_by_value(*self.SELECTORS["OCCASION_SELECT"], "10")

    def birthday_card(self, card):
        self.move_to_element(*self.SELECTORS["BIRTHDAY_CARD_TEXTAREA"])
        self.enter_text(*self.SELECTORS["BIRTHDAY_CARD_TEXTAREA"], card)

    def add_picture(self):
        # Need to add a picture
        pass

    def click_continue(self):
        self.move_to_element(*self.SELECTORS["CONTINUE_BUTTON"])
        self.click_element(*self.SELECTORS["CONTINUE_BUTTON"])

    def click_now(self):
        self.click_element(*self.SELECTORS["CLICK_NOW_DIV"])

    def choose_sms(self):
        self.click_element(*self.SELECTORS["CHOOSE_SMS_SVG"])
        self.click_element(*self.SELECTORS["SMS_INPUT"])
        self.enter_text(*self.SELECTORS["SMS_INPUT"], "0525369535")

    def gift_sender(self):
        self.move_to_element(*self.SELECTORS["GIFT_SENDER_INPUT"])
        self.enter_text(*self.SELECTORS["GIFT_SENDER_INPUT"], self.name)
        self.assert_input(*self.SELECTORS["GIFT_SENDER_INPUT"], self.name)

# from BasePage import BasePage
# from selenium.webdriver.common.by import By
#
# class SendGifts(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.name = "ofir"
#         self.driver.get("https://buyme.co.il/money/752649?price=300")
#
#     def receiver_name(self):
#         self.enter_text(By.CSS_SELECTOR, "input[title='שם מקבל המתנה']", "ohad")
#
#     def occasion(self):
#         self.select_by_value(By.CSS_SELECTOR, "select[name='eventType']", "10")
#
#     def birthday_card(self, card):
#         self.move_to_element(By.CSS_SELECTOR, "textarea[data-parsley-group='voucher-greeting']")
#         self.enter_text(By.CSS_SELECTOR, "textarea[data-parsley-group='voucher-greeting']", card)
#
#     def add_picture(self):
#         # Need to add a picture
#         pass
#
#     def click_continue(self):
#         self.move_to_element(By.CSS_SELECTOR, "button[gtm='המשך']")
#         self.click_element(By.CSS_SELECTOR, "button[gtm='המשך']")
#
#     def click_now(self):
#         self.click_element(By.CSS_SELECTOR, "div[gtm='עכשיו']")
#
#     def choose_sms(self):
#         self.click_element(By.CSS_SELECTOR, "svg[gtm='method-sms']")
#         self.click_element(By.CSS_SELECTOR, "input[id=sms]")
#         self.enter_text(By.CSS_SELECTOR, "input[id=sms]", "0525369535")
#
#     def gift_sender(self):
#         self.move_to_element(By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']")
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']", self.name)
#         self.assert_input(By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']", self.name)
