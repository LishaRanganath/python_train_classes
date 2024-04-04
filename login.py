import time
from base import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):
        def __init__(self,driver):
            super().__init__(driver)

        def login_user(self,username,password):
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.sleep_for_seconds()
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.sleep_for_seconds()
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            self.sleep_for_seconds()