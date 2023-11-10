from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from datetime import timedelta

class BasePage:
    TIMEOUT = 30

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=self.TIMEOUT)

    def wait_for_element_to_appear(self, element):
        self.wait.until(EC.visibility_of(element))