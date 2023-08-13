from BasePage import BasePage
from selenium.webdriver.common.by import By

class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"

    def sign_in(self):
        self.click_element(By.CLASS_NAME, "notSigned")
        self.click_element(By.CSS_SELECTOR, "input[placeholder='מייל']")
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='מייל']", "ofirfirst@gmail.com")
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='סיסמה']", "Ofirfirst3000")
        self.click_element(By.CSS_SELECTOR, "button[gtm='כניסה ל-BUYME']")

    def select_price(self):
        self.select_by_value(By.CSS_SELECTOR, "select[data-parsley-id='85']",
                             value="2")

    def select_area(self):
        self.select_by_value(By.XPATH, "/html/body/div[5]/div/header/div[3]/div/div/form/label[2]/div/select",
                             value="11")

    def select_category(self):
        self.select_by_value(By.CSS_SELECTOR, "select[name=category]",
                             value="419")

    def click_search(self):
        self.click_element(By.CSS_SELECTOR, "a[href='https://buyme.co.il/search']")

    # Pick Business

    # def assert_url(self):
    #     assert self.driver.current_url == "https://buyme.co.il/search?budget=2&category=419&region=11"
    #
    # def click_business(self):
    #     self.click_element(By.CSS_SELECTOR, "a[href='https://buyme.co.il/supplier/752649?bu"
    #                                         "dget=1&category=419&query=&region=9']")
    #
    # def set_present_price(self):
    #     self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", "300")
    #
    # def click_choose(self):
    #     self.click_element(By.CSS_SELECTOR, "button[gtm='בחירה']")

    # Sender receiver info

