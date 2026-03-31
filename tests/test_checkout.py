import allure
import pytest

from page_objects.home import HomePage
from page_objects.login import LoginPage
from page_objects.products import Products
from tests.test_base import TestBase
from config.config import Testdata


class TestCheckout(TestBase):

    # def setup_method(self, method):
    #     self.login_page = LoginPage(self.driver)
    #     self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
    #     self.individual_products = self.product_page.click_product_backpack()
    #     self.individual_products.click_add_cart_product()
    #     self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
    #     self.checkout = self.shopping_cart_page.click_checkout_btn()

    def login_navigate_to_checkout_backpack_product(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_backpack()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
        self.checkout = self.shopping_cart_page.click_checkout_btn()

    def login_navigate_to_checkout_back_light_product(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_bike_light()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
        self.checkout = self.shopping_cart_page.click_checkout_btn()

    @allure.title("Verify the page title")
    @allure.severity(allure.severity_level.MINOR)
    def test_product_page_title(self):
        """To Check title of checkout page"""
        self.login_navigate_to_checkout_backpack_product()
        title = self.checkout.get_product_page_title(Testdata.login_page_title)
        print(title)
        assert title == Testdata.login_page_title

    @allure.title("Verify the text present on the web page")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_shopping_cart_page_text(self):
        """This do login and go to checkout page and verify the checkout text and left right corner"""
        self.login_navigate_to_checkout_backpack_product()
        title = self.checkout.is_present()
        print(title, Testdata.checkout_page_text)
        assert title == Testdata.checkout_page_text

    @allure.title("Verify the logo text present on the web page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shopping_cart_logo_text(self):
        """This do login and go to shopping cart page and verify the at top middle Swag labs is present or not"""
        self.login_navigate_to_checkout_backpack_product()
        title = self.checkout.is_logo_text_present()
        print(title, Testdata.login_page_title)
        assert title

    @allure.title("Verify if able to add address on the web page")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_enter_name_and_address(self):
        """This do login and go to products page and verify the at top middle Swag labs is present or not"""
        self.login_navigate_to_checkout_backpack_product()
        self.checkout.enter_name_and_address(Testdata.address_first_name,
                                                       Testdata.address_last_name, Testdata.address_postal)
        # print(title, Testdata.login_page_title)

    @allure.title("Verify continue button present on the web page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enter_address_details_continue_for_backpack(self):
        """This do login and go to products page add address details and click continue"""
        self.login_navigate_to_checkout_backpack_product()
        self.checkout.enter_name_and_address(Testdata.address_first_name,
                                             Testdata.address_last_name, Testdata.address_postal)
        self.checkout.click_continue_btn()

    @allure.title("Verify continue button present on the web page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enter_address_details_continue_for_back_light(self):
        """This do login and go to products page add address details and click continue"""
        self.login_navigate_to_checkout_back_light_product()
        self.checkout.enter_name_and_address(Testdata.address_first_name,
                                             Testdata.address_last_name, Testdata.address_postal)
        self.checkout.click_continue_btn()