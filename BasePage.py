from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import allure
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Setting maximum of 10 seconds of keeping the found elements
        self.driver.implicitly_wait(10)
        # Setting up a count for the screenshots added to the allure
        self.my_screenshots = 1

    def click_element(self, locator_type, locator_value):
        try:
            # Click on element
            self.driver.find_element(locator_type, locator_value).click()
        except NoSuchElementException:
            self.screenshot()

    def enter_text(self, locator_type, locator_value, text):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            # Clearing the text box
            element.clear()
            # Entering the text after the elements clear
            element.send_keys(text)
        except NoSuchElementException:
            self.screenshot()

    def move_to_element(self, locator_type, locator_value):
        try:
            action = ActionChains(self.driver)
            my_button = self.driver.find_element(locator_type, locator_value)
            # Moving to and element
            action.move_to_element(my_button).perform()
        except NoSuchElementException:
            self.screenshot()

    def select_by_text(self, locator_type, locator_value, value):
        try:
            select = Select(self.driver.find_element(locator_type, locator_value))
            # Selects by value
            select.select_by_value(value)
        except NoSuchElementException:
            self.screenshot()

    def force_click(self, locator_type, locator_value):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            # Forcing a click on not intractable element
            self.driver.execute_script("arguments[0].click();", element)
        except NoSuchElementException:
            self.screenshot()

    def assert_input(self, locator_type, locator_value, name):
        try:
            # Getting the element
            element = self.driver.find_element(locator_type, locator_value)
            # Asserting the value for element
            assert element.get_attribute("value") == name
        except NoSuchElementException:
            self.screenshot()

    def send_photo(self, locator_type, locator_value, value):
        try:
            element = self.driver.find_element(locator_type, locator_value)
            # Sending a photo to
            element.send_keys(value)
        except NoSuchElementException:
            self.screenshot()

    def screenshot(self):
        # Adding a screenshot to the Allure Report
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Element not found {self.my_screenshots}", attachment_type=allure.attachment_type.PNG)
        self.my_screenshots += 1
