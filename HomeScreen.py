from BasePage import BasePage
from selenium.webdriver.common.by import By


class HomeScreen(BasePage):
    SELECTORS = {
        "NOT_SIGNED": (By.CLASS_NAME, "notSigned"),
        "EMAIL_INPUT": (By.CSS_SELECTOR, "input[placeholder='מייל']"),
        "PASSWORD_INPUT": (By.CSS_SELECTOR, "input[placeholder='סיסמה']"),
        "LOGIN_BUTTON": (By.CSS_SELECTOR, "button[gtm='כניסה ל-BUYME']"),
        "PRICE_SELECT_CLICK": (By.CSS_SELECTOR, "span[title='סכום']"),
        "PRICE_CLICK": (By.CSS_SELECTOR, "li[value='2']"),
        "AREA_SELECT": (By.XPATH, "//*[@id='ember1088']/div/div[1]/span"),
        "AREA_SELECT_CLICK": (By.CSS_SELECTOR, "li[value='11']"),
        "CATEGORY_SELECT": (By.CSS_SELECTOR, "select[name='category']"),
        "CATEGORY_SELECT_CLICK": (By.CSS_SELECTOR, "li[value='419']"),
        "SEARCH_LINK": (By.XPATH, "//*[@id='ember1199']")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def sign_in(self):
        # Click signup/login on Homescreen
        self.click_element(*self.SELECTORS["NOT_SIGNED"])
        # Entering email
        self.enter_text(*self.SELECTORS["EMAIL_INPUT"], "mashumashu@gmail.com")
        # Entering password
        self.enter_text(*self.SELECTORS["PASSWORD_INPUT"], "Mashumashu")
        # Click login
        self.click_element(*self.SELECTORS["LOGIN_BUTTON"])

    def select_price(self):
        # Click on price
        self.force_click(*self.SELECTORS["PRICE_SELECT_CLICK"])
        # Choosing 100-199 shekel
        self.force_click(*self.SELECTORS["PRICE_CLICK"])

    def select_area(self):
        # Click on area
        self.force_click(*self.SELECTORS["AREA_SELECT"])
        # Choosing "מרכז"
        self.force_click(*self.SELECTORS["AREA_SELECT_CLICK"])

    def select_category(self):
        # Click on catergotry
        self.force_click(*self.SELECTORS["CATEGORY_SELECT"])
        # Choosing "מתנות למזל גדי"
        self.force_click(*self.SELECTORS["CATEGORY_SELECT_CLICK"])

    def click_search(self):
        # Click on search
        self.force_click(*self.SELECTORS["SEARCH_LINK"])
