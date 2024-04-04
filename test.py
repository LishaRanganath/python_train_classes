import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(7)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys(("admin123"))


driver.find_element(By.XPATH,"//button[@type='submit']").click();
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item']/child::span[text()='Leave']").click();
driver.find_element(By.XPATH,"//a[text()='Apply']").click();

driver.find_elements(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")[0].click();
time.sleep(1)
driver.find_element(By.XPATH,"//div[@role='option']/child::span[text()='CAN - FMLA']").click()

driver.find_elements(By.XPATH,"//input[@placeholder='yyyy-dd-mm']")[0].send_keys('2024-05-04')
time.sleep(1)

to_date=driver.find_elements(By.XPATH,"//input[@placeholder='yyyy-dd-mm']")[1]
time.sleep(1)
to_date.send_keys(Keys.CONTROL + "a")
to_date.send_keys(Keys.BACKSPACE)
time.sleep(1)
to_date.send_keys('2024-07-04')
time.sleep(1)

driver.find_elements(By.XPATH,"//div[@class='oxd-select-text--after']//i")[1].click()
time.sleep(1)

driver.find_element(By.XPATH,"//div[@class='oxd-select-option']/child::span[text()='End Day Only']").click()
driver.find_elements(By.XPATH,"//div[@class='oxd-select-text--after']//i")[2].click()
time.sleep(1)

driver.find_element(By.XPATH,"//div[@class='oxd-select-option']/child::span[text()='Half Day - Afternoon']").click()
driver.find_element(By.XPATH,"//textarea").send_keys("leave for 2 days")
time.sleep(1)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[text()='My Leave']").click();
time.sleep(1)
driver.find_element(By.XPATH,"//div[text()='leave for 2 days']/parent::div/following-sibling::div/div/li/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[text()='View Leave Details']").click()
time.sleep(1)
length=len(driver.find_elements(By.XPATH,"//button[text()=' Cancel ']"))
for i in range(length):
    driver.find_elements(By.XPATH, "//button[text()=' Cancel ']")[i].click()
# time.sleep(1)
# driver.find_elements(By.XPATH,"//button[text()=' Cancel ']")[1].click()
# time.sleep(1)
# driver.find_elements(By.XPATH,"//button[text()=' Cancel ']")[2].click()
# time.sleep(1)
# driver.find_elements(By.XPATH,"//button[text()=' Cancel ']")[3].click()
# time.sleep(1)
# driver.find_elements(By.XPATH,"//button[text()=' Cancel ']")[4].click()

print(length)
print(driver.title)

input()

driver.close()

# //li[@class='oxd-calendar-selector-month']/child::i[@class='oxd-icon bi-caret-down-fill oxd-icon-button__icon']
# <div data-v-40acfd38="" data-v-13cf171c="" role="listbox" class="oxd-select-dropdown --positon-bottom" loading="false">
# <div data-v-d130bb63="" data-v-13cf171c="" role="option" class="oxd-select-option">-- Select --</div>
# <div data-v-d130bb63="" data-v-13cf171c="" role="option" class="oxd-select-option --selected">
# <span data-v-13cf171c="">CAN - FMLA</span></div></div>

