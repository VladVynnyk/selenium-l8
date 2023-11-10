from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from . import BasePage

class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.email_input = driver.find_element(By.ID, "EmailAddress")
        self.password_input = driver.find_element(By.ID, "Password")
        self.signin_button = driver.find_element(By.ID, "signin")

    def enter_email(self, email):
        self.email_input.clear()
        self.email_input.send_keys(email)

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def click_signin_button(self):
        self.signin_button.click()