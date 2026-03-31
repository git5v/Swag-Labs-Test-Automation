import pytest
import platform, sys, selenium
from config.config import Testdata
from page_objects.login import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestBase:

    pass

# @pytest.fixture
# def shopping_cart_page(init_driver):
#     # driver = request.cls.driver  # Access driver from the test class
#     login_page = LoginPage(init_driver)
#     product_page = login_page.do_login(Testdata.username, Testdata.password)
#     individual_products = product_page.add_product_backpack()
#     shopping_cart_page = individual_products.click_shopping_cart_icon()
#     return shopping_cart_page