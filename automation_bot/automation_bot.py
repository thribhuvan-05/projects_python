from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://example.com/login")

time.sleep(2)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("your_username")
password.send_keys("your_password")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(5)

print("Login automation completed")

driver.quit()


