from BasePage import BasePage
from selenium.webdriver.common.by import By

class PickBusiness(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"

    def assert_url(self):
        assert self.driver.current_url == "https://buyme.co.il/search?budget=2&category=419&region=11"

    def click_business(self):
        self.force_click(By.CLASS_NAME, "product-card-bg")

    def set_present_price(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", "300")

    def click_choose(self):
        self.force_click(By.CSS_SELECTOR, "button[gtm='בחירה']")
