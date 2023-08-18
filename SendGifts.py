from selenium.webdriver.common.by import By
from BasePage import BasePage

class SendGifts(BasePage):
    SELECTORS = {
        "RECEIVER_NAME_INPUT": (By.CSS_SELECTOR, "input[tuaandiinputdiscrp='שם מקבל המתנה. כדי לשלוח את המתנה אליך. נווט אחורה ושנה את הבחירה בכפתורי הרדיו']"),
        "OCCASION_SELECT": (By.CSS_SELECTOR, "span[alt='לאיזה אירוע?']"),
        "OCCASION_SELECT_CLICK": (By.CSS_SELECTOR, "li[value='10']"),
        "BIRTHDAY_CARD_TEXTAREA": (By.CSS_SELECTOR, "textarea[data-parsley-group='voucher-greeting']"),
        "PHOTO_UPLOAD": (By.CSS_SELECTOR, "input[type='file']"),
        "CONTINUE_BUTTON": (By.CSS_SELECTOR, "button[gtm='המשך']"),
        "CHOOSE_SMS_SVG": (By.CSS_SELECTOR, "svg[gtm='method-sms']"),
        "SMS_INPUT": (By.CSS_SELECTOR, "input[id=sms]"),
        "GIFT_SENDER_INPUT": (By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']"),
        "CLICK_NOW_DIV": (By.CSS_SELECTOR, "div[gtm='עכשיו']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"

    def receiver_name(self):
        self.enter_text(*self.SELECTORS["RECEIVER_NAME_INPUT"], "ohad")

    def occasion(self):
        self.click_element(*self.SELECTORS["OCCASION_SELECT"])
        self.force_click(*self.SELECTORS["OCCASION_SELECT_CLICK"])
        # self.select_by_text(*self.SELECTORS["OCCASION_SELECT"], "יום הולדת")

    def birthday_card(self, card):
        self.move_to_element(*self.SELECTORS["BIRTHDAY_CARD_TEXTAREA"])
        self.enter_text(*self.SELECTORS["BIRTHDAY_CARD_TEXTAREA"], card)

    def add_picture(self):
        filepath = "/Users/ofirzvishaboo/Downloads/my_logo.png"
        self.move_to_element(*self.SELECTORS["PHOTO_UPLOAD"])
        self.send_photo(*self.SELECTORS["PHOTO_UPLOAD"], filepath)

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
