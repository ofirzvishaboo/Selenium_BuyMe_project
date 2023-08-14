from selenium.webdriver.common.by import By
from BasePage import BasePage

class PickBusiness(BasePage):
    SELECTORS = {
        "BUSINESS_CARD": (By.CLASS_NAME, "product-card-bg"),
        "PRESENT_PRICE_INPUT": (By.CSS_SELECTOR, "input[placeholder='הכנס סכום']"),
        "CHOOSE_BUTTON": (By.CSS_SELECTOR, "button[gtm='בחירה']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://buyme.co.il/search?budget=2&category=419&region=11")

    def assert_url(self):
        assert self.driver.current_url == "https://buyme.co.il/search?budget=2&category=419&region=11"

    def click_business(self):
        self.force_click(*self.SELECTORS["BUSINESS_CARD"])

    def set_present_price(self):
        self.enter_text(*self.SELECTORS["PRESENT_PRICE_INPUT"], "300")

    def click_choose(self):
        self.force_click(*self.SELECTORS["CHOOSE_BUTTON"])

# from BasePage import BasePage
# from selenium.webdriver.common.by import By
#
# class PickBusiness(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver.get("https://buyme.co.il/search?budget=2&category=419&region=11")
#
#     def assert_url(self):
#         assert self.driver.current_url == "https://buyme.co.il/search?budget=2&category=419&region=11"
#
#     def click_business(self):
#         self.force_click(By.CLASS_NAME, "product-card-bg")
#
#     def set_present_price(self):
#         self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", "300")
#
#     def click_choose(self):
#         self.force_click(By.CSS_SELECTOR, "button[gtm='בחירה']")
