from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# inport jeda waktu
import time


#Positive Case Login

driver = webdriver.Chrome()
driver.maximize_window()

# menambahkan alamat url
driver.get("https://www.saucedemo.com/")

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

#Klik button
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

#Pilih Dropdown

dropdown_element = driver.find_element(By.CLASS_NAME, 'product_sort_container')

dropdown = Select(dropdown_element)
dropdown.select_by_index('1')

time.sleep(5)

driver.quit()