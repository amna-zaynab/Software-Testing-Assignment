from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# ChromeDriver path
service = Service("C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = "https://opensource-demo.orangehrmlive.com/"

def open_login():
    driver.get(url)
    time.sleep(2)

def enter_credentials(username, password):
    driver.find_element(By.NAME,"username").clear()
    driver.find_element(By.NAME,"username").send_keys(username)

    driver.find_element(By.NAME,"password").clear()
    driver.find_element(By.NAME,"password").send_keys(password)

    driver.find_element(By.TAG_NAME,"button").click()
    time.sleep(3)

# ---------------------------
# TC01 Valid Login
# ---------------------------
open_login()
enter_credentials("Admin","admin123")
print("TC01 Valid Login Tested")
driver.back()

# ---------------------------
# TC02 Invalid Password
# ---------------------------
open_login()
enter_credentials("Admin","wrong123")
print("TC02 Invalid Password Tested")

# ---------------------------
# TC03 Invalid Username
# ---------------------------
open_login()
enter_credentials("test","admin123")
print("TC03 Invalid Username Tested")

# ---------------------------
# TC04 Empty Username
# ---------------------------
open_login()
enter_credentials("","admin123")
print("TC04 Empty Username Tested")

# ---------------------------
# TC05 Empty Password
# ---------------------------
open_login()
enter_credentials("Admin","")
print("TC05 Empty Password Tested")

# ---------------------------
# TC06 Both Fields Empty
# ---------------------------
open_login()
enter_credentials("","")
print("TC06 Both Empty Tested")

# ---------------------------
# TC07 Logout
# ---------------------------
open_login()
enter_credentials("Admin","admin123")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Logout").click()
print("TC07 Logout Tested")

# ---------------------------
# TC08 Login Button Function
# ---------------------------
open_login()
driver.find_element(By.TAG_NAME,"button").click()
print("TC08 Login Button Tested")

# ---------------------------
# TC09 Password Masking
# ---------------------------
open_login()
driver.find_element(By.NAME,"password").send_keys("admin123")
print("TC09 Password Masking Tested")

# ---------------------------
# TC10 Access Dashboard Without Login
# ---------------------------
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(2)
print("TC10 Access Dashboard Without Login Tested")

# ---------------------------
# TC11 Case Sensitive Username
# ---------------------------
open_login()
enter_credentials("ADMIN","admin123")
print("TC11 Case Sensitive Username Tested")

# ---------------------------
# TC12 Case Sensitive Password
# ---------------------------
open_login()
enter_credentials("Admin","ADMIN123")
print("TC12 Case Sensitive Password Tested")

# ---------------------------
# TC13 Special Character Password
# ---------------------------
open_login()
enter_credentials("Admin","@123")
print("TC13 Special Character Password Tested")

# ---------------------------
# TC14 Long Username
# ---------------------------
open_login()
enter_credentials("verylongusernameexampletest123","admin123")
print("TC14 Long Username Tested")

# ---------------------------
# TC15 Refresh After Logout
# ---------------------------
open_login()
enter_credentials("Admin","admin123")
driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Logout").click()
driver.refresh()
print("TC15 Refresh After Logout Tested")

driver.quit()