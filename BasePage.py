from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        element = self.driver.find_element(locator_type, locator_value)
        element.click()

    def enter_text(self, locator_type, locator_value, text):
        element = self.driver.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def move_to_element(self, locator_type, locator_value):
        action = ActionChains(self.driver)
        my_button = self.driver.find_element(locator_type, locator_value)
        action.move_to_element(my_button).perform()

    def select_by_value(self, locator_type, locator_value, value):
        select = Select(self.driver.find_element(locator_type, locator_value))
        select.select_by_value(value)

    def wait_for_appear(self, locator_type, locator_value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(
            self.driver.find_element(locator_type, locator_value)))
