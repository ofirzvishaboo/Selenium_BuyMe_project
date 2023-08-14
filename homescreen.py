from BasePage import BasePage
from selenium.webdriver.common.by import By

class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://buyme.co.il/")

    def sign_in(self):
        self.click_element(By.CLASS_NAME, "notSigned")
        self.click_element(By.CSS_SELECTOR, "input[placeholder='מייל']")
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='מייל']", "ofirfirst@gmail.com")
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='סיסמה']", "Ofirfirst3000")
        self.click_element(By.CSS_SELECTOR, "button[gtm='כניסה ל-BUYME']")

    def select_price(self):
        self.select_by_value(By.XPATH, "//*[@id='ember2540']/div/select", value="2")
        # self.force_click(By.XPATH, "//*[@id='ember3347']")
        # self.click_element(By.CSS_SELECTOR, "span[alt='סכום']")

    def select_area(self):
        self.select_by_value(By.XPATH, "/html/body/div[5]/div/header/div[3]/div/div/form/label[2]/div/select",
                             value="11")
        # self.click_element(By.CSS_SELECTOR, "span[alt='אזור']")
        # self.force_click(By.CSS_SELECTOR, "//*[@id='ember2585']/span")


    def select_category(self):
        self.select_by_value(By.CSS_SELECTOR, "select[name=category]",
                             value="419")

    def click_search(self):
        self.click_element(By.CSS_SELECTOR, "a[href='https://buyme.co.il/search']")
