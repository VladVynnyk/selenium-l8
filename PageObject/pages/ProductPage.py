from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from . import BasePage, ProductPage

class ProductPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.change_size_button = driver.find_element(By.XPATH, "//select[contains(@id, 'variantSelector')]")
        self.m_size = driver.find_element(By.XPATH, "//option[contains(@value, '204516917')]")
        self.green_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='add-button']")
        self.bug_message = driver.find_element(By.CSS_SELECTOR, "[data-testid='bag-error-message']")

    def change_size(self):
        self.change_size_button.click()
        self.m_size.click()
        return self
    
    def click_on_green_button(self):
        self.green_button.click()
        return self
    
    def get_bug_message(self):
        message = self.bug_message()
        return message.text