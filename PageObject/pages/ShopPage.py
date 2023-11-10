from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from . import BasePage, ProductPage

class ShopPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.product_button = driver.find_element(By.XPATH, "//a[contains(@href, '/the-north-face/the-north-face-nuptse-cropped-down-puffer-jacket-in-black/prd/204516879#colourWayId-204516904')]")

    def click_on_product_button(self):
        self.product_button.click()
        return ProductPage(self.driver)