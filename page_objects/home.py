from selenium.webdriver.common.by import By

from config.config import Testdata
from page_objects.base_page import BasePage


class HomePage(BasePage):
    # locators
    user_guide_txt = (By.CLASS_NAME, "Header__Heading-sc-1q6ll6r-6 lgEQnJ")
    account_name = (By.ID, "hs-global-toolbar-accounts")
    setting_icon = (By.ID, "hs-global-toolbar-settings-list-item")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)

    def home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_visible(self):
        self.is_visible(self.setting_icon)

    def get_header_value(self):
        if self.is_visible(self.user_guide_txt):
            return self.get_element_text(self.user_guide_txt)

    def get_account_name(self):
        if self.is_visible(self.account_name):
            return self.get_element_text(self.account_name)


