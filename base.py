from selenium import webdriver
import time
driver=webdriver.Chrome()
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def sleep_for_seconds(self,seconds=1):
        time.sleep(seconds)
