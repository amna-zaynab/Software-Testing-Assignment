from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(3)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.TAG_NAME,"button").click()

print("Login successful")

time.sleep(5)

driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT,"Logout").click()

print("Logout successful")

driver.quit()