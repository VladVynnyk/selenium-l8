from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from . import BasePage

class RegisterPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.human_icon = driver.find_element(By.CSS_SELECTOR, "[data-testid='myAccountIcon']")
        self.email_input = driver.find_element(By.ID, "Email")
        self.first_name_input = driver.find_element(By.ID, "FirstName")
        self.last_name_input = driver.find_element(By.ID, "LastName")
        self.password_input = driver.find_element(By.ID, "Password")
        self.password_input = driver.find_element(By.ID, "Password")
        self.birthday = driver.find_element(By.ID, "BirthDay")
        self.birthmonth = driver.find_element(By.ID, "BirthMonth")
        self.birth_year = driver.find_element(By.ID, "BirthYear")
        self.input_for_male_clothes = driver.find_element(By.ID, "male")
        self.continue_button = driver.find_element(By.ID, "register")
        self.day_option = driver.find_element(By.XPATH, "//option[contains(@value, '1')]")
        self.month_option = driver.find_element(By.XPATH, "//option[contains(text(), 'January')]")
        self.year_option = driver.find_element(By.XPATH, "//option[contains(@value, '1998')]")
    
    def enter_email(self, email):
        self.email_input.clear()
        self.email_input.send_keys(email)

    def enter_first_name(self, first_name):
        self.first_name_input.clear()
        self.first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        self.last_name_input.clear()
        self.last_name_input.send_keys(last_name)

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def select_birth_date(self):
        self.birthday.click()
        self.day_option.click()
        self.birthmonth.click()
        self.month_option.click()
        self.birth_year.click()
        self.year_option.click()

    def select_male_clothes(self):
        self.input_for_male_clothes.click()

    def click_continue_button(self):
        self.continue_button.click()