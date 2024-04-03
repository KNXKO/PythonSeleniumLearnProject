from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
count_ofcookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Odkliknutie prvotného okna ak sa zobrazí
try:
    input_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fc-primary-button"))
    )
    input_element.click()
except NoSuchElementException:
    print("Prvotné okno nebolo nájdené.")

# Pocka kym najde element a odklikne
try:
    setLang = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='langSelect-EN']"))
    )
    setLang.click()
except:
    print("Element s id='langSelect-EN' nebol nájdený.")

time.sleep(3)

cookie = driver.find_element(By.ID, cookie_id)

while True:
    try:
        cookie.click()
    except StaleElementReferenceException:
        cookie = driver.find_element(By.ID, cookie_id)
        cookie.click()

    count_ofcookies = driver.find_element(By.ID, count_ofcookies_id).text.split(" ")[0]
    count_ofcookies = int(count_ofcookies.replace(",",""))

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if count_ofcookies >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break