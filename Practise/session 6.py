from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
# try:
#     username = driver.find_element(By.NAME, "username")
#     username.send_keys("Admin")
# except Exception as e:
#     print(f"Error {e}")
username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
time.sleep(2)
#-Password Imput Field
password= driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys("admin123")
#Logi_btn
time.sleep(2)
login_btn = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
login_btn.click()

#search_btn
time.sleep(2)
searchbtn= driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > div > div > input")
searchbtn.send_keys("Admin")
time.sleep(2)
click_Admin= driver.find_element(By.LINK_TEXT,"Admin")
click_Admin.click()
# driver = webdriver.Chrome(executable_path="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")
driver.quit()
