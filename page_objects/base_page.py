import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""This is the parent of all pages"""
"""It contain all generic config and utilities"""

class BasePage:
    def __init__(self, driver):   # driver comes from the test files where it defined like LoginPage(self.driver)
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def javascript_scroll_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def take_screenshot_attach_allure(self, img_name):
        time.sleep(0.5)
        allure.attach(
            self.driver.get_screenshot_as_png(),  # Get screenshot as PNG bytes
            name=img_name,  # Name in the Allure report
            attachment_type=allure.attachment_type.PNG
        )

    def attach_allure_text(self, name):
        allure.attach(body=name,
                      name="Extracted plain text content",
                      attachment_type=allure.attachment_type.TEXT)

