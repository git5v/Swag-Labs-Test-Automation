# import pytest
#
# from page_objects.home import HomePage
# from page_objects.login import LoginPage
# from tests.test_base import TestBase
# from config.config import Testdata
#
#
# class TestHome(TestBase):
#
#     def test_home_page_title(self):
#         self.login_page = LoginPage(self.driver)
#         self.home_page = self.login_page.do_login(Testdata.username, Testdata.password)
#         title = self.home_page.get_title(Testdata.home_page_title)
#         assert title == Testdata.home_page_title
#
#     def test_home_page_header(self):
#         self.login_page = LoginPage(self.driver)
#         self.home_page = self.login_page.do_login(Testdata.username, Testdata.password)
#         header_text = self.home_page.get_header_value()
#         assert header_text == Testdata.home_page_header
#
#     def test_account_name(self):
#         self.login_page = LoginPage(self.driver)
#         self.home_page = self.login_page.do_login(Testdata.username, Testdata.password)
#         account_name = self.home_page.get_account_name()
#         assert account_name == Testdata.account_name
#
#     def test_setting_icon(self):
#         self.login_page = LoginPage(self.driver)
#         self.home_page = self.login_page.do_login(Testdata.username, Testdata.password)
#         return self.home_page.is_setting_icon_visible()