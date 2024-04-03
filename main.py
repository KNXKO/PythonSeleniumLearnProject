from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Presmerovanie na stránku
driver.get("https://google.com")

# Kliknutie na uvodne google okno
input_element = driver.find_element(By.ID, "L2AGLb")
input_element.click()

# Napisanie do search baru "lukas lechovic"
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("lukas lechovic" + Keys.ENTER)

time.sleep(7)
driver.quit()