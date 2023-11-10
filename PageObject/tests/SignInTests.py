import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages import HomePage, LoginPage 

class CreateAccountTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.asos.com/women/")

    def tearDown(self):
        self.driver.quit()

    def sign_in_test(self):
        home_page = HomePage(self.driver)

        home_page.hover_on_human_icon()
        login_page = home_page.click_on_sign_in_button()
        self.assertIsInstance(login_page, LoginPage)

        login_page.enter_email("test@example.com")
        login_page.enter_password("testpassword")
        login_page.click_signin_button()


if __name__ == "__main__":
    unittest.main()