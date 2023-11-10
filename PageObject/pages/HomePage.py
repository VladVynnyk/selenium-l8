import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from . import BasePage, RegisterPage, ShopPage


class HomePage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.human_icon = driver.find_element(By.CSS_SELECTOR, "[data-testid='myAccountIcon']")
        self.join_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Join')]")
        self.signin_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='signin-link']")
        self.winter_button = driver.find_element(By.CSS_SELECTOR, "[data-id='5811d5c8-03b2-4bf3-bf0d-e4471f8e5a46']")
        self.puffer_jackets = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.asos.com/women/coats-jackets/puffer-jackets/cat/?cid=28643')]")

    def hover_on_human_icon(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.human_icon).perform()
        time.sleep(3)
        return self

    def click_on_join_button(self):
        self.join_button.click()
        return RegisterPage(self.driver)
    
    def click_on_sign_in_button(self):
        self.signin_link.click()
        return self
    
    def click_on_jacket_button(self):
        self.winter_button.click()
        self.puffer_jackets.click()
        return ShopPage(self.driver)