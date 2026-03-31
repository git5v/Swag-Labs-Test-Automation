from selenium.webdriver.common.by import By
import time
from page_objects.base_page import BasePage
from config.config import Testdata
from page_objects.home import HomePage
from page_objects.shopping_cart import ShoppingCart


class IndividualProducts(BasePage):
    # locators
    swag_labs_app_logo_text = (By.CLASS_NAME, "app_logo")
    price_vale_text = (By.CLASS_NAME, "inventory_details_price")
    add_prod_btn = (By.ID, "add-to-cart")
    remove_prod_btn = (By.ID, "remove")
    shopping_cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)

    def get_ind_product_page_title(self, title):
        """To get the individual product page title"""
        self.take_screenshot_attach_allure(img_name="individual product page screen")
        return self.get_title(title)

    def get_price_value(self):
        """To get price of the product"""
        self.take_screenshot_attach_allure(img_name="individual product page screen")
        return self.get_element_text(self.price_vale_text)

    def click_add_cart_product(self):
        """To perform click on add button"""
        self.take_screenshot_attach_allure(img_name="individual product page screen add to cart logo")
        self.do_click(self.add_prod_btn)
        # time.sleep(10)

    def click_remove_cart_product(self):
        """To perform click on remove button"""
        self.take_screenshot_attach_allure(img_name="individual product page screen add remove button")
        self.do_click(self.remove_prod_btn)
        time.sleep(2)

    def click_shopping_cart_icon(self):
        """To perform click on shopping cart button"""
        self.do_click(self.shopping_cart_icon)
        self.take_screenshot_attach_allure(img_name="individual product page screen shopping cart button")
        time.sleep(2)
        return ShoppingCart(self.driver)