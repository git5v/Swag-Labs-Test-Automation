from selenium.webdriver.common.by import By
import time
from page_objects.base_page import BasePage
from config.config import Testdata
from page_objects.checkout_overview import CheckoutOverview
from page_objects.home import HomePage
# from page_objects.individual_product import individualProducts


class Checkout(BasePage):
    # locators
    # username = (By.ID, "user-name")
    # password = (By.ID, "password")
    # login_btn = (By.ID, "login-button")
    # create_acc = (By.LINK_TEXT, "Get started free")
    swag_labs_app_logo_text = (By.CLASS_NAME, "app_logo")
    checkout_title = (By.CLASS_NAME, "title")
    first_name_input_txt = (By.ID, "first-name")
    last_name_input_txt = (By.ID, "last-name")
    postal_input_txt = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")

    # backpack_product = (By.ID, "item_4_title_link")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)

    def get_product_page_title(self, title):
        """To get the product page title"""
        self.take_screenshot_attach_allure(img_name="checkout page screen")
        return self.get_title(title)

    def is_present(self):
        """To check if the your cart text is present on shopping cart page"""
        self.take_screenshot_attach_allure(img_name="checkout page screen")
        return self.get_element_text(self.checkout_title)

    def is_logo_text_present(self):
        """To check if the logo text is present"""
        self.take_screenshot_attach_allure(img_name="checkout page screen")
        return self.is_visible(self.swag_labs_app_logo_text)

    def enter_name_and_address(self, first_name, last_name, postal):
        """Enter first name, last name and postal address"""
        self.take_screenshot_attach_allure(img_name="checkout page screen before entering address details")
        self.do_send_keys(self.first_name_input_txt, first_name)
        self.do_send_keys(self.last_name_input_txt, last_name)
        self.do_send_keys(self.postal_input_txt, postal)
        self.take_screenshot_attach_allure(img_name="checkout page screen after entering address details")


    def click_continue_btn(self):
        """Click continue button"""
        self.do_click(self.continue_btn)
        self.take_screenshot_attach_allure(img_name="checkout page screen")
        return CheckoutOverview(self.driver)
        # next page
