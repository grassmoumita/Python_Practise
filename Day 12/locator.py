from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()      #maximize of the window
time.sleep(5)


#by Link_Text
# linktext = driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc")
# linktext.click()
# time.sleep(5)

#by partical link test
# par_linktext = driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM")
# par_linktext.click()
# time.sleep(5)

#to check the length of all links by Findelements
# links= driver.find_elements(By.TAG_NAME,"a")
# print(len(links))

#locator using css selector
#tag + class combination

x=driver.find_element(By.CSS_SELECTOR,"input.oxd-input")
x.send_keys("Admin")
time.sleep(5)


driver.quit()

