from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import allure
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.my_screenshots = 1

    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, locator_value).click()
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def enter_text(self, locator_type, locator_value, text):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            element.clear()
            element.send_keys(text)
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def move_to_element(self, locator_type, locator_value):
        try:
            action = ActionChains(self.driver)
            my_button = self.driver.find_element(locator_type, locator_value)
            action.move_to_element(my_button).perform()
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def select_by_text(self, locator_type, locator_value, value):
        select = Select(self.driver.find_element(locator_type, locator_value))
        select.select_by_value(value)

    def force_click(self, locator_type, locator_value):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            self.driver.execute_script("arguments[0].click();", element)
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def assert_input(self, locator_type, locator_value, name):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            assert element.get_attribute("value") == name
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def send_photo(self, locator_type, locator_value, value):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            element.send_keys(value)
        except NoSuchElementException:
            self.screenshot(f"Element_not_found{self.my_screenshots}")

    def screenshot(self, name):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
        self.my_screenshots += 1
