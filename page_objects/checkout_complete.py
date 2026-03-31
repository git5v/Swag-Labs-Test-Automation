from selenium.webdriver.common.by import By
import time
from page_objects.base_page import BasePage
from config.config import Testdata
from page_objects.home import HomePage
# from page_objects.individual_product import individualProducts


class CheckoutComplete(BasePage):
    # locators
    # username = (By.ID, "user-name")
    # password = (By.ID, "password")
    # login_btn = (By.ID, "login-button")
    # create_acc = (By.LINK_TEXT, "Get started free")
    swag_labs_app_logo_text = (By.CLASS_NAME, "app_logo")
    checkout_title = (By.CLASS_NAME, "title")
    order_complete_text = (By.CLASS_NAME, "complete-header")


    # backpack_product = (By.ID, "item_4_title_link")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)

    def get_product_page_title(self, title):
        """To get the checkout complete page title"""
        self.take_screenshot_attach_allure(img_name="checkout complete page screen")
        return self.get_title(title)

    def is_present(self):
        """To check if the your cart text is present on checkout complete page"""
        self.take_screenshot_attach_allure(img_name="checkout complete page screen")
        return self.get_element_text(self.checkout_title)

    def is_logo_text_present(self):
        """To check if the logo text is present"""
        self.take_screenshot_attach_allure(img_name="checkout complete page screen")
        return self.is_visible(self.swag_labs_app_logo_text)

    def compare_order_complete_text(self, order_complete_text):
        """Enter first name, last name and postal address"""
        self.take_screenshot_attach_allure(img_name="checkout complete page screen")
        actual_product_text = self.get_element_text(self.order_complete_text)
        print(actual_product_text)
        return bool(actual_product_text == order_complete_text)


