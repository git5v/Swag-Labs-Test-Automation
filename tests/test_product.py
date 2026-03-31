import allure
import pytest

from page_objects.home import HomePage
from page_objects.login import LoginPage
from page_objects.products import Products
from tests.test_base import TestBase
from config.config import Testdata


class TestProduct(TestBase):

    def perform_login(self):
        """Perform login operation"""
        self.login_page = LoginPage(self.driver)
        self.product_page = self.login_page.do_login(Testdata.username, Testdata.password)

    @allure.title("Verify the page title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_page_title(self):
        """This do login and check product page title"""
        self.perform_login()
        title = self.product_page.get_product_page_title(Testdata.login_page_title)
        assert title == Testdata.login_page_title

    @allure.title("Verify the text present on the web page")
    @allure.severity(allure.severity_level.MINOR)
    def test_product_page_text(self):
        """This do login and go to products page and verify the Product text and left right corner"""
        self.perform_login()
        title = self.product_page.is_present()
        print(title, Testdata.product_page_text)
        assert title == Testdata.product_page_text

    @allure.title("Verify the logo text present on the web page")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_product_page_logo_text(self):
        """This do login and go to products page and verify the at top middle Swag labs is present or not"""
        self.perform_login()
        title = self.product_page.is_logo_text_present()
        print(title, Testdata.login_page_title)
        assert title

    @allure.title("Verify if able to add backpack product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_product_backpack(self):
        """for adding the backpack product"""
        self.perform_login()
        new_page = self.product_page.click_product_backpack()
        # print(title, Testdata.login_page_title)
        # assert title

    @allure.title("Verify if able to add back light product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_product_bike_light(self):
        """for adding bike light product"""
        self.perform_login()
        new_page = self.product_page.click_product_bike_light()

    @allure.title("Verify if able to add tshirt product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_product_tshirt(self):
        """for adding bike tshirt product"""
        self.perform_login()
        new_page = self.product_page.click_product_tshirt()

    @allure.title("Verify if able to add jacket product")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_product_jacket(self):
        """for adding jacket product"""
        self.perform_login()
        new_page = self.product_page.click_product_jacket()

    @allure.title("Verify if sidebar menu is present")
    @allure.severity(allure.severity_level.CRITICAL)
    # sidebar menu
    def test_verify_sidebar_present(self):
        """for checking the cancel button present or not on sidebar menu"""
        self.perform_login()
        self.product_page.click_check_sidebar_menu()

    @allure.title("Verify if about page is present in sidebar menu")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_about_page_is_present(self):
        """for clickng the about page from sidebar menu"""
        self.perform_login()
        self.product_page.navigate_sidebar_menu()
        self.product_page.navigate_to_about_page()
        # allure.attach(
        #     self.driver.get_screenshot_as_png(),  # Get screenshot as PNG bytes
        #     name="about_page",  # Name in the Allure report
        #     attachment_type=allure.attachment_type.PNG
        # )

    @allure.title("Verify logout functionality from sidebar menu")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_perform_logout(self):
        """for checking the cancel button present or not on sidebar menu"""
        self.perform_login()
        self.product_page.navigate_sidebar_menu()
        self.product_page.perform_logout()
