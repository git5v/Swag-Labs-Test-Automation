import allure
import pytest

from page_objects.home import HomePage
from page_objects.login import LoginPage
from page_objects.products import Products
from tests.test_base import TestBase
from config.config import Testdata


class TestCheckoutComplete(TestBase):

    # to make test bed ready for backpack product
    def navigate_backpack_product(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_backpack()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
        self.checkout = self.shopping_cart_page.click_checkout_btn()
        self.checkout.enter_name_and_address(Testdata.address_first_name,
                                             Testdata.address_last_name, Testdata.address_postal)
        self.checkout_overview = self.checkout.click_continue_btn()
        self.checkout_complete = self.checkout_overview.click_finish_btn()

    # to make test bed ready for backpack product
    def navigate_back_light_product(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_bike_light()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
        self.checkout = self.shopping_cart_page.click_checkout_btn()
        self.checkout.enter_name_and_address(Testdata.address_first_name,
                                             Testdata.address_last_name, Testdata.address_postal)
        self.checkout_overview = self.checkout.click_continue_btn()
        self.checkout_complete = self.checkout_overview.click_finish_btn()

    @allure.title("Verify the page title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_complete_page_title(self):
        """To Check title of shopping cart page"""
        self.navigate_backpack_product()
        title = self.checkout_complete.get_product_page_title(Testdata.login_page_title)
        print(title)
        assert title == Testdata.login_page_title

    @allure.title("Verify the checkout complete text on the web page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_complete_text(self):
        """This do login and go to checkout complete and verify the Product text and left right corner"""
        self.navigate_backpack_product()
        title = self.checkout_complete.is_present()
        print(title, Testdata.checkout_complete_text)
        assert title == Testdata.checkout_complete_text

    @allure.title("Verify the logo text present on the web page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shopping_cart_logo_text(self):
        """This do login and go to checkout complete and verify the at top middle Swag labs is present or not"""
        self.navigate_backpack_product()
        title = self.checkout_complete.is_logo_text_present()
        print(title, Testdata.login_page_title)
        assert title

    @allure.title("Verify the order complete text on the web page")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_compare_order_complete_text_backpack(self):
        """This do login and go to checkout complete page and verify complete order is present or not"""
        self.navigate_backpack_product()
        self.checkout_complete.compare_order_complete_text(Testdata.order_complete_text)

    # @allure.title("Verify the order complete text on the web page")
    # @allure.severity(allure.severity_level.BLOCKER)
    # def test_compare_order_complete_text_back_light(self):
    #     """This do login and go to checkout complete page and verify complete order is present or not"""
    #     self.navigate_back_light_product()
    #     self.checkout_complete.compare_order_complete_text(Testdata.order_complete_text)
