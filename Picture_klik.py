from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# inport jeda waktu
import time

#Positive Case Login

driver = webdriver.Chrome()
driver.maximize_window()

# menambahkan alamat url
driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, timeout=30, poll_frequency=5, ignored_exceptions=[NoSuchElementException])

#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="login_credentials"]/h4')
teks_elemen = element.text

if element.text == "Accepted usernames are:":
    print("Berhasil masuk ke page login")
else:
    print("Validasi teks gagal")

time.sleep(2)

#Input Email dan Password
driver.find_element("xpath",'//*[@id="user-name"]').send_keys("standard_user")
driver.find_element("xpath",'//*[@id="password"]').send_keys("secret_sauce")
time.sleep(2)

#Klik button Login
elem = driver.find_element("xpath",'//*[@id="login-button"]')
elem.click()

time.sleep(2)



#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
teks_elemen = element.text

if element.text == "Products":
    print("Berhasil Login")
else:
    print("Test Case 1 Gagal")

#Klik Foto product
#elem = driver.find_element("xpath",'//*[@id="item_4_img_link"]/img')

element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="item_4_img_link"]/img')))
element.click()

time.sleep(2)

element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart"]')))
element.click()

time.sleep(2)

driver.quit()