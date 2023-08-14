from BasePage import BasePage
from selenium.webdriver.common.by import By

class HomeScreen(BasePage):
    SELECTORS = {
        "NOT_SIGNED": (By.CLASS_NAME, "notSigned"),
        "EMAIL_INPUT": (By.CSS_SELECTOR, "input[placeholder='מייל']"),
        "PASSWORD_INPUT": (By.CSS_SELECTOR, "input[placeholder='סיסמה']"),
        "LOGIN_BUTTON": (By.CSS_SELECTOR, "button[gtm='כניסה ל-BUYME']"),
        "PRICE_SELECT": (By.XPATH, "//*[@id='ember1053']/div/select"),
        "AREA_SELECT": (By.XPATH, "/html/body/div[5]/div/header/div[3]/div/div/form/label[2]/div/select"),
        "CATEGORY_SELECT": (By.CSS_SELECTOR, "select[name=category]"),
        "SEARCH_LINK": (By.CSS_SELECTOR, "a[href='https://buyme.co.il/search']")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def sign_in(self):
        self.click_element(*self.SELECTORS["NOT_SIGNED"])
        self.click_element(*self.SELECTORS["EMAIL_INPUT"])
        self.enter_text(*self.SELECTORS["EMAIL_INPUT"], "mashumashu@gmail.com")
        self.enter_text(*self.SELECTORS["PASSWORD_INPUT"], "Mashumashu")
        self.click_element(*self.SELECTORS["LOGIN_BUTTON"])

    def select_price(self):
        self.select_by_text(*self.SELECTORS["PRICE_SELECT"], value='100-199 ש"ח')

    def select_area(self):
        self.select_by_text(*self.SELECTORS["AREA_SELECT"], value="מרכז")

    def select_category(self):
        self.select_by_text(*self.SELECTORS["CATEGORY_SELECT"], value="מתנות למזל אריה")

    def click_search(self):
        self.click_element(*self.SELECTORS["SEARCH_LINK"])
