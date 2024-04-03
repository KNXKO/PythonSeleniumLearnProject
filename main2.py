from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Presmerovanie na stránku
driver.get("https://google.com")

# Pocka kym najde element a odklikne
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "L2AGLb"))
)
input_element = driver.find_element(By.ID, "L2AGLb")
input_element.click()

# Napisanie do search baru "lukas lechovic"
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("lukas lechovic" + Keys.ENTER)

# Pocka kym sa vyhladá text a klikne
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Lukáš Lechovič KNXKO"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Lukáš Lechovič KNXKO")
link.click()

time.sleep(7)
driver.quit()