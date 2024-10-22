#Testcase - Open the browser using username and password, after that need to check the dashboard title

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# serve_obj=Service("C:\Drivers\chrome-win64\chrome_proxy.exe")
driver = webdriver.Chrome()     # driver is an object, chrome() is a class of webdriver module
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")   #1st step to open the browser

time.sleep(5)
username=driver.find_element(By.NAME, "username")
username.send_keys("Admin")
time.sleep(5)
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

loginbutton = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
loginbutton.click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("login test passed")
else:
    print("login test failed")

driver.quit()