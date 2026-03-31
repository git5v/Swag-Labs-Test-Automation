from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")
element = driver.find_element(By.ID, "submit")

driver.switch_to.new_window('tab')
driver.get("https://www.python.org")

print(driver.title)
driver.quit()