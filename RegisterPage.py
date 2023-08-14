from selenium.webdriver.common.by import By
from BasePage import BasePage

class RegisterPage(BasePage):
    SELECTORS = {
        "NOT_SIGNED": (By.CLASS_NAME, "notSigned"),
        "SIGNUP_TEXT": (By.CSS_SELECTOR, "span[aria-label='להרשמה']"),
        "NAME_INPUT": (By.CSS_SELECTOR, "input[placeholder='שם פרטי']"),
        "EMAIL_INPUT": (By.CSS_SELECTOR, "input[placeholder='מייל']"),
        "PASSWORD_INPUT": (By.CSS_SELECTOR, "input[placeholder='סיסמה']"),
        "CONFIRM_PASSWORD_INPUT": (By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']"),
        "LOGIN_CHECKBOX": (By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']"),
        "SUBMIT_BUTTON": (By.CSS_SELECTOR, "button[gtm='הרשמה ל-BUYME']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"
        self.driver.get("https://buyme.co.il/")

    def click_signup_button(self):
        self.click_element(*self.SELECTORS["NOT_SIGNED"])

    def click_signup_text(self):
        self.click_element(*self.SELECTORS["SIGNUP_TEXT"])

    def enter_name(self):
        self.enter_text(*self.SELECTORS["NAME_INPUT"], self.name)

    def enter_mail(self):
        self.enter_text(*self.SELECTORS["EMAIL_INPUT"], "mashumashu@gmail.com")

    def enter_password(self):
        self.enter_text(*self.SELECTORS["PASSWORD_INPUT"], "Ofirfirst3000")

    def enter_password_confirmation(self):
        self.enter_text(*self.SELECTORS["CONFIRM_PASSWORD_INPUT"], "Ofirfirst3000")

    def click_login_checkbox(self):
        self.click_element(*self.SELECTORS["LOGIN_CHECKBOX"])

    def click_submit(self):
        self.move_to_element(*self.SELECTORS["SUBMIT_BUTTON"])
        self.click_element(*self.SELECTORS["SUBMIT_BUTTON"])

    def firstname_assertion(self):
        self.assert_input(*self.SELECTORS["NAME_INPUT"], self.name)
# from selenium.webdriver.common.by import By
# from BasePage import BasePage
#
# class RegisterPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.name = "ofir"
#         self.driver.get("https://buyme.co.il/")
#
#     # Click the "notSigned" element
#     def click_signup_button(self):
#         self.click_element(By.CLASS_NAME, "notSigned")
#
#     def click_signup_text(self):
#         # Click the signup text
#         self.click_element(By.XPATH, "//*[@id='ember964']/div/div[1]/div[2]/div/div[3]/div[1]/span")
#
#     def enter_name(self):
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='שם פרטי']", self.name)
#
#     def enter_mail(self):
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='מייל']", "mashumashu@gmail.com")
#
#     def enter_password(self):
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='סיסמה']", "Ofirfirst3000")
#
#     def enter_password_confirmation(self):
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']", "Ofirfirst3000")
#
#     def click_login_checkbox(self):
#         self.click_element(By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']")
#         # button = WebDriverWait(self.driver, 10).until(
#         #     EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']")))
#         # button.click()
#
#     def click_submit(self):
#         self.move_to_element(By.CSS_SELECTOR, "button[gtm='הרשמה ל-BUYME']")
#         self.click_element(By.CSS_SELECTOR, "button[gtm='הרשמה ל-BUYME']")
#         # action = ActionChains(self.driver)
#         # my_button = self.driver.find_element(By.CSS_SELECTOR, "button[gtm='הרשמה ל-BUYME']")
#         # action.move_to_element(my_button).perform()
#
#     def firstname_assertion(self):
#         # Assert that the name field contains the value "ofir"
#         self.assert_input(By.CSS_SELECTOR, "input[placeholder='שם פרטי']", self.name)
