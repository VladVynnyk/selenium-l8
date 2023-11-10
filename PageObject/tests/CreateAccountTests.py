import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages import HomePage, RegisterPage 

class CreateAccountTests(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver and navigate to the homepage
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.asos.com/women/")

    def tearDown(self):
        # Close the WebDriver after the test
        self.driver.quit()

    def create_account_test(self):
        home_page = HomePage(self.driver)

        home_page.hover_on_human_icon()
        register_page = home_page.click_on_join_button()
        self.assertIsInstance(register_page, RegisterPage)

        register_page.enter_email("test@example.com")
        register_page.enter_first_name("John")
        register_page.enter_last_name("Doe")
        register_page.enter_password("testpassword")
        register_page.select_birth_data()
        register_page.select_male_clothes()
        register_page.click_continue_button()


if __name__ == "__main__":
    unittest.main()