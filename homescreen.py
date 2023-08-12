from BasePage import BasePage
from selenium.webdriver.common.by import By

class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"

    def select_price(self):
        self.select_by_value(By.XPATH, "/html/body/div[5]/div/header/div[3]/div/div/form/label[1]/div/select",
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

    def assert_url(self):
        assert self.driver.current_url == "https://buyme.co.il/search?budget=1&category=419&region=9"

    def click_business(self):
        self.click_element(By.CSS_SELECTOR, "a[href='https://buyme.co.il/supplier/752649?bu"
                                            "dget=1&category=419&query=&region=9']")

    def set_present_price(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", "300")

    def click_choose(self):
        self.click_element(By.CSS_SELECTOR, "button[gtm='בחירה']")

    # Sender receiver info

    def receiver_name(self):
        self.enter_text(By.ID, "ember2754", "ohad")

    def occasion(self):
        self.select_by_value(By.CSS_SELECTOR, "select[name='eventType']", "10")

    def birthday_card(self, card):
        self.enter_text(By.CSS_SELECTOR, "textarea[class='parsley-success']", card)

    def add_picture(self):
        # Need to add a picture
        pass

    def click_continue(self):
        self.click_element(By.ID, "ember2775")

    def click_now(self):
        self.click_element(By.CSS_SELECTOR, "div[gtm='עכשיו']")

    def choose_sms(self):
        self.click_element(By.CSS_SELECTOR, "svg[gtm='method-sms']")
        self.wait_for_appear(By.CSS_SELECTOR, "input[id=sms]")
        self.enter_text(By.CSS_SELECTOR, "input[id=sms]", "0525369535")

    def gift_sender(self):
        sender_name = self.enter_text(By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']", self.name)
        assert sender_name.get_attribute("value") == self.name
