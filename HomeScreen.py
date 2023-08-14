# from BasePage import BasePage
# from selenium.webdriver.common.by import By
#
# class HomeScreen(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver.get("https://buyme.co.il/")
#
#     def sign_in(self):
#         self.click_element(By.CLASS_NAME, "notSigned")
#         self.click_element(By.CSS_SELECTOR, "input[placeholder='מייל']")
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='מייל']", "ofirfirst@gmail.com")
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='סיסמה']", "Ofirfirst3000")
#         self.click_element(By.CSS_SELECTOR, "button[gtm='כניסה ל-BUYME']")
#
#     def select_price(self):
#         self.select_by_value(By.XPATH, "//*[@id='ember2540']/div/select", value="2")
#         # self.force_click(By.XPATH, "//*[@id='ember3347']")
#         # self.click_element(By.CSS_SELECTOR, "span[alt='סכום']")
#
#     def select_area(self):
#         self.select_by_value(By.XPATH, "/html/body/div[5]/div/header/div[3]/div/div/form/label[2]/div/select",
#                              value="11")
#         # self.click_element(By.CSS_SELECTOR, "span[alt='אזור']")
#         # self.force_click(By.CSS_SELECTOR, "//*[@id='ember2585']/span")
#
#
#     def select_category(self):
#         self.select_by_value(By.CSS_SELECTOR, "select[name=category]",
#                              value="419")
#
#     def click_search(self):
#         self.click_element(By.CSS_SELECTOR, "a[href='https://buyme.co.il/search']")
from BasePage import BasePage
from selenium.webdriver.common.by import By

class HomeScreen(BasePage):
    SELECTORS = {
        "NOT_SIGNED": (By.CLASS_NAME, "notSigned"),
        "EMAIL_INPUT": (By.CSS_SELECTOR, "input[placeholder='מייל']"),
        "PASSWORD_INPUT": (By.CSS_SELECTOR, "input[placeholder='סיסמה']"),
        "LOGIN_BUTTON": (By.CSS_SELECTOR, "button[gtm='כניסה ל-BUYME']"),
        "PRICE_SELECT": (By.CSS_SELECTOR, "select[data-parsley-id='44']"),
        "AREA_SELECT": (By.XPATH, "/html/body/div[5]/div/header/div[3]/div/div/form/label[2]/div/select"),
        "CATEGORY_SELECT": (By.CSS_SELECTOR, "select[name=category]"),
        "SEARCH_LINK": (By.CSS_SELECTOR, "a[href='https://buyme.co.il/search']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://buyme.co.il/")

    def sign_in(self):
        self.click_element(*self.SELECTORS["NOT_SIGNED"])
        self.click_element(*self.SELECTORS["EMAIL_INPUT"])
        self.enter_text(*self.SELECTORS["EMAIL_INPUT"], "mashumashu@gmail.com")
        self.enter_text(*self.SELECTORS["PASSWORD_INPUT"], "Mashumashu")
        self.click_element(*self.SELECTORS["LOGIN_BUTTON"])

    def select_price(self):
        self.select_by_value(*self.SELECTORS["PRICE_SELECT"], value='2')

    def select_area(self):
        self.select_by_value(*self.SELECTORS["AREA_SELECT"], value="11")

    def select_category(self):
        self.select_by_value(*self.SELECTORS["CATEGORY_SELECT"], value="419")

    def click_search(self):
        self.click_element(*self.SELECTORS["SEARCH_LINK"])
