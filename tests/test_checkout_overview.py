import allure
import pytest

from page_objects.home import HomePage
from page_objects.login import LoginPage
from page_objects.products import Products
from tests.test_base import TestBase
from config.config import Testdata


class TestCheckoutOverview(TestBase):

    # def setup_method(self, method):
    #     self.login_page = LoginPage(self.driver)
    #     self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
    #     self.individual_products = self.product_page.click_product_backpack()
    #     self.individual_products.click_add_cart_product()
    #     self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
    #     self.checkout = self.shopping_cart_page.click_checkout_btn()
    #     self.checkout.enter_name_and_address(Testdata.address_first_name,
    #                                          Testdata.address_last_name, Testdata.address_postal)
    #     self.checkout_overview = self.checkout.click_continue_btn()

    def navigate_backpack_checkout_overview(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_backpack()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
        self.checkout = self.shopping_cart_page.click_checkout_btn()
        self.checkout.enter_name_and_address(Testdata.address_first_name,
                                             Testdata.address_last_name, Testdata.address_postal)
        self.checkout_overview = self.checkout.click_continue_btn()

    def navigate_back_light_checkout_overview(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_bike_light()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
        self.checkout = self.shopping_cart_page.click_checkout_btn()
        self.checkout.enter_name_and_address(Testdata.address_first_name,
                                             Testdata.address_last_name, Testdata.address_postal)
        self.checkout_overview = self.checkout.click_continue_btn()

    @allure.title("Verify the page title")
    @allure.severity(allure.severity_level.MINOR)
    def test_checkout_overview_page_title(self):
        """To Check title of checkout overview page"""
        self.navigate_backpack_checkout_overview()
        title = self.checkout_overview.get_product_page_title(Testdata.login_page_title)
        print(title)
        assert title == Testdata.login_page_title

    @allure.title("Verify the page text present on the web page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_overview_page_text(self):
        """This do login and go to checkout overview and verify the Product text and left right corner"""
        self.navigate_backpack_checkout_overview()
        title = self.checkout_overview.is_present()
        print(title, Testdata.checkout_overview_page_text)
        assert title == Testdata.checkout_overview_page_text

    @allure.title("Verify the logo text present on the web page")
    @allure.severity(allure.severity_level.MINOR)
    def test_checkout_overview_logo_text(self):
        """This do login and go to checkout overview page and verify the at top middle Swag labs is present or not"""
        self.navigate_backpack_checkout_overview()
        title = self.checkout_overview.is_logo_text_present()
        print(title, Testdata.login_page_title)
        assert title

    @allure.title("Verify the backpack product present on the web page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_is_present_backpack_product(self):
        """This do login and go to checkout overview and verify the backpack product is present"""
        self.navigate_backpack_checkout_overview()
        self.checkout_overview.is_present_backpack_product(Testdata.product_backpack)

    @allure.title("Verify the back light product present on the web page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_is_present_back_light_product(self):
        """This do login and go to checkout overview and verify the back light product is present"""
        self.navigate_back_light_checkout_overview()
        self.checkout_overview.is_present_back_light_product(Testdata.product_back_light)

    @allure.title("Verify the finish button present on the web page backpack for product")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_finish_btn_backpack(self):
        """This do login and go to products page and verify the finish button"""
        self.navigate_backpack_checkout_overview()
        self.checkout_overview.click_finish_btn()

    @allure.title("Verify the finish button present on the web page for back light")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_finish_btn_back_light(self):
        """This do login and go to products page and verify the finish button"""
        self.navigate_back_light_checkout_overview()
        self.checkout_overview.click_finish_btn()