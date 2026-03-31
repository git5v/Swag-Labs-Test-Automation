import allure
import pytest

from page_objects.home import HomePage
from page_objects.login import LoginPage
from page_objects.products import Products
from tests.test_base import TestBase
from config.config import Testdata


class TestProduct(TestBase):

    def navigate_to_ind_product_backpack(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_prod = self.product_page.click_product_backpack()

    def navigate_to_ind_product_bike_light(self):
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        self.individual_prod = self.product_page.click_product_bike_light()

    @allure.title("Verify the page title")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_ind_product_page_title(self):
        """This do login and check product page title"""
        # self.login_page = LoginPage(self.driver)
        # self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        # self.individual_prod = self.product_page.click_product_backpack()
        self.navigate_to_ind_product_backpack()
        title = self.individual_prod.get_ind_product_page_title(Testdata.login_page_title)
        self.product_page.attach_allure_text(title)
        assert title == Testdata.login_page_title

    @allure.title("Verify the individual product page backpack product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_product_backpack(self):
        """This do login and go to products page and click on product go into ind product backpack page"""
        # self.login_page = LoginPage(self.driver)
        # self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        # self.individual_prod = self.product_page.click_product_backpack()
        self.navigate_to_ind_product_backpack()
        # print(title, Testdata.login_page_title)
        self.individual_prod.click_add_cart_product()

    @allure.title("Verify the remove individual product page backpack product")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_product_backpack(self):
        """This do login and go to products page and click on product go into ind product backpack page and remove"""
        # self.login_page = LoginPage(self.driver)
        # self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        # self.individual_prod = self.product_page.click_product_backpack()
        # print(title, Testdata.login_page_title)
        self.navigate_to_ind_product_backpack()
        self.individual_prod.click_add_cart_product()
        self.individual_prod.click_remove_cart_product()


    @allure.title("Verify the individual product page bike light product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_product_backlight(self):
        """This do login and go to products page and click on product go into ind product bike light page"""
        self.navigate_to_ind_product_bike_light()
        # print(title, Testdata.login_page_title)
        self.individual_prod.click_add_cart_product()

    @allure.title("Verify the remove individual product page bike light product")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_product_backpack(self):
        """This do login and go to products page and click on product go into ind product bike light page and remove"""
        self.navigate_to_ind_product_bike_light()
        self.individual_prod.click_add_cart_product()
        self.individual_prod.click_remove_cart_product()


    # test add_product tshirt, jacket and remove_product_bike_light, tshirt, jacket

    @allure.title("Verify the click on shopping cart icon individual product page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shopping_cart_icon(self):
        """This do login and go to products page and verify the at top middle Swag labs is present or not"""
        # self.login_page = LoginPage(self.driver)
        # self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)
        # self.individual_prod = self.product_page.click_product_backpack()
        # print(title, Testdata.login_page_title)
        self.navigate_to_ind_product_backpack()
        self.individual_prod.click_add_cart_product()
        self.individual_prod.click_shopping_cart_icon()

    @allure.title("Verify the price of backpack on individual product page")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_price_backpack(self):
        self.navigate_to_ind_product_backpack()
        # print(title, Testdata.login_page_title)
        price_val_text = self.individual_prod.get_price_value()
        print("this is value", price_val_text)
        print(Testdata.backpack_product_price)
        assert price_val_text == Testdata.backpack_product_price


