import allure
import pytest

from page_objects.home import HomePage
from page_objects.login import LoginPage
from tests.test_base import TestBase
from config.config import Testdata


class TestLogin(TestBase):

    @allure.title("Verify the login button present on web page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_btn_visible(self):
        """To test login button is present on the login page or not"""
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_present()
        # print(flag)
        assert flag

    @allure.title("Verify the text present on the web page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_page_title_text(self):
        """To test title of the login page"""
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_login_title(Testdata.login_page_title)
        # print(title)
        assert title == Testdata.login_page_title

    @allure.title("Verify user can log in with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        """To test the login using username and password"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(Testdata.username, Testdata.password)
