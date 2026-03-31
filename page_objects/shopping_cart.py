from selenium.webdriver.common.by import By
import time
from page_objects.base_page import BasePage
from config.config import Testdata
from page_objects.checkout import Checkout
from page_objects.home import HomePage
# from page_objects.individual_product import individualProducts


class ShoppingCart(BasePage):
    # locators
    # username = (By.ID, "user-name")
    # password = (By.ID, "password")
    # login_btn = (By.ID, "login-button")
    # create_acc = (By.LINK_TEXT, "Get started free")
    swag_labs_app_logo_text = (By.CLASS_NAME, "app_logo")
    shopping_cart_title = (By.CLASS_NAME, "title")
    backpack_product = (By.PARTIAL_LINK_TEXT, "Sauce Labs Backpack")
    bike_light_product = (By.LINK_TEXT, "Sauce Labs Bike Light")
    backpack_product_text = "Sauce Labs Backpack"
    back_light_product_text = "Sauce Labs Bike Light"
    bike_tshirt_product = (By.LINK_TEXT, "Sauce Labs Bolt T-Shirt")
    bike_jacket_product = (By.LINK_TEXT, "Sauce Labs Fleece Jacket")
    checkout_btn = (By.ID, 'checkout')

    # backpack_product = (By.ID, "item_4_title_link")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)

    def get_product_page_title(self, title):
        """To get the shopping cart page title"""
        self.take_screenshot_attach_allure(img_name="shopping cart page screen")
        return self.get_title(title)

    def is_present(self):
        """To check if the your cart text is present on shopping cart page"""
        self.take_screenshot_attach_allure(img_name="shopping cart page screen")
        return self.get_element_text(self.shopping_cart_title)

    def is_logo_text_present(self):
        """To check if the logo text is present"""
        self.take_screenshot_attach_allure(img_name="shopping cart page screen")
        return self.is_visible(self.swag_labs_app_logo_text)

    def verify_backpack_product_text(self):
        """To check product text in shopping cart"""
        self.take_screenshot_attach_allure(img_name="shopping cart page screen")
        actual_product_text = self.get_element_text(self.backpack_product)
        print(actual_product_text)
        return bool(actual_product_text == self.backpack_product_text)

    def verify_back_light_product_text(self):
        """To check product text in shopping cart"""
        self.take_screenshot_attach_allure(img_name="shopping cart page screen")
        actual_product_text = self.get_element_text(self.bike_light_product)
        print(actual_product_text)
        return bool(actual_product_text == self.back_light_product_text)

    def click_checkout_btn(self):
        """To product text in shopping cart"""
        self.take_screenshot_attach_allure(img_name="shopping cart page screen")
        self.do_click(self.checkout_btn)
        self.take_screenshot_attach_allure(img_name="checkout page screen")
        return Checkout(self.driver)
        # next page
