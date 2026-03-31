import allure
import pytest

from page_objects.home import HomePage
from page_objects.login import LoginPage
from page_objects.products import Products
from tests.test_base import TestBase
from config.config import Testdata


class TestShoppingCart(TestBase):

    def login_navigate_to_shopping_cart_backpack(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_backpack()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()

    def login_navigate_to_shopping_cart_bike_light(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_products = self.product_page.click_product_bike_light()
        self.individual_products.click_add_cart_product()
        self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()

    @allure.title("Verify the page title")
    @allure.severity(allure.severity_level.MINOR)
    def test_product_page_title(self):
        """To Check title of shopping cart page"""
        # self.login_page = LoginPage(self.driver)
        # self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        # self.individual_products = self.product_page.add_product_backpack()
        # self.shopping_cart_page = self.individual_products.click_shopping_cart_icon()
        self.login_navigate_to_shopping_cart_backpack()
        title = self.shopping_cart_page.get_product_page_title(Testdata.login_page_title)
        print(title)
        assert title == Testdata.login_page_title

    @allure.title("Verify the text present on the web page")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_shopping_cart_page_text(self):
        """This do login and go to products page and verify the Product text and left right corner"""
        self.login_navigate_to_shopping_cart_backpack()
        title = self.shopping_cart_page.is_present()
        print(title, Testdata.shopping_cart_page_text)
        assert title == Testdata.shopping_cart_page_text

    @allure.title("Verify the logo text present on the web page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shopping_cart_logo_text(self):
        """This do login and go to shopping cart page and verify the at top middle Swag labs is present or not"""
        self.login_navigate_to_shopping_cart_backpack()
        title = self.shopping_cart_page.is_logo_text_present()
        print(title, Testdata.login_page_title)
        assert title

    @allure.title("Verify the product text present on the web page shopping cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_backpack_product_text_shopping_cart(self):
        """This will perform login add backpack product go to shopping cart and verify the product text"""
        self.login_navigate_to_shopping_cart_backpack()
        title = self.shopping_cart_page.verify_backpack_product_text()
        print(title, Testdata.login_page_title)
        # assert title

    # ---------
    @allure.title("Verify the backpack product text present on the web page shopping cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_backpack_product_text_shopping_cart(self):
        """This will perform login add backpack product go to shopping cart and verify the product text"""
        self.login_navigate_to_shopping_cart_backpack()
        title = self.shopping_cart_page.verify_backpack_product_text()
        print(title, Testdata.login_page_title)

    @allure.title("Verify the bike light product text present on the web page shopping cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_bike_light_product_text_shopping_cart(self):
        """This will perform login add bike light product go to shopping cart and verify the product text"""
        self.login_navigate_to_shopping_cart_bike_light()
        title = self.shopping_cart_page.verify_back_light_product_text()
        print(title, Testdata.login_page_title)
    # test for shopping cart tshirt, jacket and remove_product_bike_light, tshirt, jacket
    # ---------
    @allure.title("Verify the checkout button present on the web page for backapack product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_backpack_product_text_shopping_cart_click_checkout_btn(self):
        """This will chek checkout button"""
        self.login_navigate_to_shopping_cart_backpack()
        self.shopping_cart_page.click_checkout_btn()

    @allure.title("Verify the checkout button present on the web page for bike light product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_bike_light_product_text_shopping_cart_click_checkout_btn(self):
        """This will chek checkout button"""
        self.login_navigate_to_shopping_cart_bike_light()
        self.shopping_cart_page.click_checkout_btn()