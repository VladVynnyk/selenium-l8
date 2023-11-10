import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages import HomePage, ShopPage, ProductPage

class CreateAccountTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.asos.com/women/")

    def tearDown(self):
        self.driver.quit()

    def create_account_test(self):
        home_page = HomePage(self.driver)

        home_page.hover_on_human_icon()
        shop_page = home_page.click_on_jacket_button()
        self.assertIsInstance(shop_page, ShopPage)

        product_page = shop_page.click_on_product_button()
        self.assertIsInstance(product_page, ProductPage)
        
        product_page.change_size()
        product_page.click_on_green_button()
        message = product_page.get_bug_massage()
        self.assertEqual(message.text, "Sorry, there was an issue adding this item to the bag, please try again.")


if __name__ == "__main__":
    unittest.main()