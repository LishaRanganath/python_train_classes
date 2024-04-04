from selenium import webdriver
from login import Login
from leave_navigate import Leave
class HRM:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(7)
        self.login_page=Login(self.driver)
        self.apply_leave=Leave(self.driver)

    def login(self,username,password):
        self.login_page.login_user(username,password)

    def leave(self,link1,link2):
        self.apply_leave.leave_page(link1,link2)

    def applying_leave_(self):
        self.apply_leave.apply_leave_page()

hrm = HRM()
hrm.login("Admin", "admin123")
link1="//a[@class='oxd-main-menu-item']/child::span[text()='Leave']"
link2="//a[text()='Apply']"
hrm.leave(link1,link2)
hrm.applying_leave_()