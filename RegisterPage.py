from selenium.webdriver.common.by import By
from BasePage import BasePage


class RegisterPage(BasePage):
    SELECTORS = {
        "NOT_SIGNED": (By.CSS_SELECTOR, "a[aria-label='כניסה / הרשמה']"),
        "SIGNUP_TEXT": (By.XPATH, "//*[@id='ember964']/div/div[1]/div[2]/div/div[3]/div[1]/span"),
        "NAME_INPUT": (By.CSS_SELECTOR, "input[placeholder='שם פרטי']"),
        "EMAIL_INPUT": (By.CSS_SELECTOR, "input[placeholder='מייל']"),
        "PASSWORD_INPUT": (By.CSS_SELECTOR, "input[placeholder='סיסמה']"),
        "CONFIRM_PASSWORD_INPUT": (By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']"),
        "LOGIN_CHECKBOX": (By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']"),
        "SUBMIT_BUTTON": (By.CSS_SELECTOR, "button[gtm='הרשמה ל-BUYME']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        # Setting my name for assertion later
        self.name = "ofir"

    def click_signup_button(self):
        # Click on signuo/login
        self.click_element(*self.SELECTORS["NOT_SIGNED"])

    def click_signup_text(self):
        # Click on signup text
        self.click_element(*self.SELECTORS["SIGNUP_TEXT"])

    def enter_name(self):
        # Enters first name
        self.enter_text(*self.SELECTORS["NAME_INPUT"], self.name)

    def enter_mail(self):
        # Enters Email address
        self.enter_text(*self.SELECTORS["EMAIL_INPUT"], "forifnnri@gmail.com")

    def enter_password(self):
        # Enters Password
        self.enter_text(*self.SELECTORS["PASSWORD_INPUT"], "Ohoh1123654")

    def enter_password_confirmation(self):
        # Entering password confirmation
        self.enter_text(*self.SELECTORS["CONFIRM_PASSWORD_INPUT"], "Ohoh1123654")

    def click_login_checkbox(self):
        # Click on stay logged in checkbox
        self.click_element(*self.SELECTORS["LOGIN_CHECKBOX"])

    def click_submit(self):
        # Moving to the submit button
        self.move_to_element(*self.SELECTORS["SUBMIT_BUTTON"])
        # Click on Submit button
        self.click_element(*self.SELECTORS["SUBMIT_BUTTON"])

    def firstname_assertion(self):
        # Asserting the first name was correct
        self.assert_input(*self.SELECTORS["NAME_INPUT"], self.name)
