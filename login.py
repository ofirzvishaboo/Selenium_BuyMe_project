from selenium.webdriver.common.by import By
from BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = "ofir"

    # Click the "notSigned" element
    def click_signup_button(self):
        self.click_element(By.CLASS_NAME, "notSigned")
        # self.driver.find_element(By.CLASS_NAME, value="notSigned").click()

    def click_signup_text(self):
        # Click the signup text
        self.click_element(By.XPATH, "/html/body/div[5]/div/div[1]/div[2]/div/div[3]/div[1]/span")
        # signup_button = self.driver.find_element(By.XPATH, "//*[@id='ember964']/div/div[1]/div[2]/div/div[3]/div[1]/span")
        # signup_button.click()

    def enter_name(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='שם פרטי']", self.name)

    def enter_mail(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='מייל']", "mashumashu@gmail.com")

    def enter_password(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='סיסמה']", "Ofirfirst3000")

    def enter_password_confirmation(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']", "Ofirfirst3000")

    # def enter_name(self):
    #     # firstname = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='שם פרטי']")
    #     # firstname.clear()
    #     # firstname.send_keys(self.name)
    #
    # def enter_mail(self):
    #     mail_name = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='מייל']")
    #     mail_name.clear()
    #     mail_name.send_keys("ofirfirst@gmail.com")
    #
    # def enter_password(self):
    #     passw = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='סיסמה']")
    #     passw.clear()
    #     passw.send_keys("Ofirfirst3000")
    #
    # def enter_password_confirmation(self):
    #     passw1 = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']")
    #     passw1.clear()
    #     passw1.send_keys("Ofirfirst3000")

# The following code will wait for the button to be visible before clicking it.
    # This will help to prevent errors caused by the button not being ready yet.
    def click_login_checkbox(self):
        self.click_element(By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']")
        # button = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']")))
        # button.click()

    def click_submit(self):
        submit_button = (By.CSS_SELECTOR, "button[gtm='הרשמה ל-BUYME']")
        self.move_to_element(submit_button)
        self.click_element(submit_button)
        # action = ActionChains(self.driver)
        # my_button = self.driver.find_element(By.CSS_SELECTOR, "button[gtm='הרשמה ל-BUYME']")
        # action.move_to_element(my_button).perform()

    def firstname_assertion(self):
        firstname = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='שם פרטי']")
        # Assert that the name field contains the value "ofir"
        assert firstname.get_attribute("value") == self.name
