import allure
from selenium.webdriver.common.by import By
import time
from page_objects.base_page import BasePage
from config.config import Testdata
from page_objects.home import HomePage
from page_objects.individual_product import IndividualProducts


class Products(BasePage):
    # locators
    # username = (By.ID, "user-name")
    # password = (By.ID, "password")
    # login_btn = (By.ID, "login-button")
    # create_acc = (By.LINK_TEXT, "Get started free")
    swag_labs_app_logo_text = (By.CLASS_NAME, "app_logo")
    products_title_text = (By.CLASS_NAME, "title")
    backpack_product = (By.PARTIAL_LINK_TEXT, "Sauce Labs Backpack")
    bike_light_product = (By.LINK_TEXT, "Sauce Labs Bike Light")
    bike_tshirt_product = (By.LINK_TEXT, "Sauce Labs Bolt T-Shirt")
    bike_jacket_product = (By.LINK_TEXT, "Sauce Labs Fleece Jacket")

    # sidebar menu
    hamburger_menu_btn = (By.ID, "react-burger-menu-btn")
    cancel_menu_page = (By.ID, "react-burger-cross-btn")
    about_menu_link = (By.ID, "about_sidebar_link")
    logout_menu_link = (By.ID, "logout_sidebar_link")

    # backpack_product = (By.ID, "item_4_title_link")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)

    def get_product_page_title(self, title):
        """To get the product page title"""
        self.take_screenshot_attach_allure(img_name="product page screen")
        self.attach_allure_text(title)
        return self.get_title(title)

    def is_present(self):
        """To check if the product text is present"""
        self.take_screenshot_attach_allure(img_name="product page screen")
        return self.get_element_text(self.products_title_text)

    def is_logo_text_present(self):
        """To check if the product title is present"""
        self.take_screenshot_attach_allure(img_name="product page screen")
        return self.is_visible(self.swag_labs_app_logo_text)

    def click_product_backpack(self):
        """To add backpack product"""
        self.take_screenshot_attach_allure(img_name="product page screen")
        self.javascript_scroll_click(self.backpack_product)
        time.sleep(8)
        self.take_screenshot_attach_allure(img_name="individual product page screen")
        return IndividualProducts(self.driver)

    def click_product_bike_light(self):
        """To add bike light product"""
        self.take_screenshot_attach_allure(img_name="product page screen")
        self.javascript_scroll_click(self.bike_light_product)
        self.take_screenshot_attach_allure(img_name="individual product page screen")
        time.sleep(2)
        return IndividualProducts(self.driver)

    def click_product_tshirt(self):
        """To add tshirt product"""
        self.take_screenshot_attach_allure(img_name="product page screen")
        self.javascript_scroll_click(self.bike_tshirt_product)
        self.take_screenshot_attach_allure(img_name="individual product page screen")
        time.sleep(10)
        return IndividualProducts(self.driver)

    def click_product_jacket(self):
        """To add jacket product"""
        self.take_screenshot_attach_allure(img_name="product page screen")
        self.javascript_scroll_click(self.bike_jacket_product)
        self.take_screenshot_attach_allure(img_name="individual product page screen")
        time.sleep(10)
        return IndividualProducts(self.driver)

    # sidebar menu page
    def navigate_sidebar_menu(self):
        """To navigate to sidebar menu"""
        self.do_click(self.hamburger_menu_btn)
        self.take_screenshot_attach_allure(img_name="sidemenu bar")

    def click_check_sidebar_menu(self):
        """To check if cancel button is present in sidemenu"""
        self.navigate_sidebar_menu()
        # self.do_click(self.hamburger_menu_btn)
        self.take_screenshot_attach_allure(img_name="sidebar_menu")
        return self.is_visible(self.cancel_menu_page)

    def navigate_to_about_page(self):
        """Click about page from sidebar menu"""
        self.do_click(self.about_menu_link)
        time.sleep(10)
        self.take_screenshot_attach_allure(img_name="about_page")
        # next page

    def perform_logout(self):
        """Click logout from sidebar menu"""
        self.do_click(self.logout_menu_link)
        self.take_screenshot_attach_allure(img_name="logout_screen")
        # next page