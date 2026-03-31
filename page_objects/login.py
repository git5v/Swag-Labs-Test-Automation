from selenium.webdriver.common.by import By
import time
from page_objects.base_page import BasePage
from config.config import Testdata
from page_objects.home import HomePage
from page_objects.products import Products


class LoginPage(BasePage):
    # locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    create_acc = (By.LINK_TEXT, "Get started free")
    swag_labs_logo_text = (By.CLASS_NAME, "login_logo")
    link_text = ""

    # constructor
    def __init__(self, driver):
        """passed instance of driver go to BasePage class"""
        super().__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def get_login_title(self, title):
        """To get the login page title"""
        self.take_screenshot_attach_allure(img_name="sing up screen")
        self.attach_allure_text(title)
        return self.get_title(title)

    def is_present(self):
        """To check if the login button is enabled"""
        self.take_screenshot_attach_allure(img_name="sing up screen")
        return self.is_visible(self.swag_labs_logo_text)

    def do_login(self, username, password):
        """To perform the login and return product page with driver"""
        self.take_screenshot_attach_allure(img_name="before login")
        self.do_send_keys(self.username, username)
        self.do_send_keys(self.password, password)
        self.take_screenshot_attach_allure(img_name="after entering login details")
        self.do_click(self.login_btn)
        self.take_screenshot_attach_allure(img_name="after login")
        # time.sleep(10)
        return Products(self.driver)  # returns the driver for the next page
