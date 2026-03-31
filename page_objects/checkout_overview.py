from selenium.webdriver.common.by import By
import time
from page_objects.base_page import BasePage
from config.config import Testdata
from page_objects.checkout_complete import CheckoutComplete
from page_objects.home import HomePage
# from page_objects.individual_product import individualProducts


class CheckoutOverview(BasePage):
    # locators
    # username = (By.ID, "user-name")
    # password = (By.ID, "password")
    # login_btn = (By.ID, "login-button")
    # create_acc = (By.LINK_TEXT, "Get started free")
    swag_labs_app_logo_text = (By.CLASS_NAME, "app_logo")
    checkout_title = (By.CLASS_NAME, "title")
    backpack_product_text = (By.LINK_TEXT, "Sauce Labs Backpack")
    back_light_product_text = (By.LINK_TEXT, "Sauce Labs Bike Light")
    finish_btn = (By.ID, "finish")

    # backpack_product = (By.ID, "item_4_title_link")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)

    def get_product_page_title(self, title):
        """To get the checkout overview page title"""
        self.take_screenshot_attach_allure(img_name="checkout overview page screen")
        return self.get_title(title)

    def is_present(self):
        """To check if the text is present on checkout overview page"""
        self.take_screenshot_attach_allure(img_name="checkout overview page screen")
        return self.get_element_text(self.checkout_title)

    def is_logo_text_present(self):
        """To check if the logo text is present"""
        self.take_screenshot_attach_allure(img_name="checkout overview page screen")
        return self.is_visible(self.swag_labs_app_logo_text)

    def is_present_backpack_product(self, backpack_product_text):
        """Enter first name, last name and postal address"""
        self.take_screenshot_attach_allure(img_name="checkout overview page screen")
        actual_product_text = self.get_element_text(self.backpack_product_text)
        print(actual_product_text)
        return bool(actual_product_text == backpack_product_text)

    def is_present_back_light_product(self, backpack_product_text):
        """Enter first name, last name and postal address"""
        self.take_screenshot_attach_allure(img_name="checkout overview page screen")
        actual_product_text = self.get_element_text(self.back_light_product_text)
        print(actual_product_text)
        return bool(actual_product_text == backpack_product_text)

    def click_finish_btn(self):
        """Click finish button"""
        self.do_click(self.finish_btn)
        self.take_screenshot_attach_allure(img_name="checkout Complete page screen")
        return CheckoutComplete(self.driver)
        # next page
