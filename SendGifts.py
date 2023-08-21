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
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"

    def receiver_name(self):
        # Enters receiver name
        self.enter_text(*self.SELECTORS["RECEIVER_NAME_INPUT"], "ohad")

    def occasion(self):
        # Clicks on selectbox
        self.click_element(*self.SELECTORS["OCCASION_SELECT"])
        # Choosing birthday
        self.force_click(*self.SELECTORS["OCCASION_SELECT_CLICK"])

    def birthday_card(self, card):
        # Moving to the birthday card
        self.move_to_element(*self.SELECTORS["BIRTHDAY_CARD_TEXTAREA"])
        # Enter the birthday card that i will write on the main
        self.enter_text(*self.SELECTORS["BIRTHDAY_CARD_TEXTAREA"], card)

    def add_picture(self):
        filepath = "/Users/ofirzvishaboo/Downloads/my_logo.png"
        # Moving to the photo upload
        self.move_to_element(*self.SELECTORS["PHOTO_UPLOAD"])
        # Uploading the photo
        self.send_photo(*self.SELECTORS["PHOTO_UPLOAD"], filepath)

    def click_continue(self):
        # Moving to continue button
        self.move_to_element(*self.SELECTORS["CONTINUE_BUTTON"])
        # Click on continue button
        self.click_element(*self.SELECTORS["CONTINUE_BUTTON"])

    def choose_sms(self):
        # Click on SMS
        self.click_element(*self.SELECTORS["CHOOSE_SMS_SVG"])
        # Clicks on textbox
        self.click_element(*self.SELECTORS["SMS_INPUT"])
        # Entering the text
        self.enter_text(*self.SELECTORS["SMS_INPUT"], "0525369535")

    def gift_sender(self):
        # Moving to gift sender name
        self.move_to_element(*self.SELECTORS["GIFT_SENDER_INPUT"])
        # Enters my name form init
        self.enter_text(*self.SELECTORS["GIFT_SENDER_INPUT"], self.name)
        # Asserting that i got the right name
        self.assert_input(*self.SELECTORS["GIFT_SENDER_INPUT"], self.name)
