from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
    print("Validasi teks berhasil")
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

driver.quit()


#Negative Case Login
#Email Salah

driver = webdriver.Chrome()
driver.maximize_window()

# menambahkan alamat url
driver.get("https://www.saucedemo.com/")

#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="login_credentials"]/h4')
teks_elemen = element.text

if element.text == "Accepted usernames are:":
    print("Validasi teks berhasil")
else:
    print("Validasi teks gagal")

time.sleep(2)

#Input Email dan Password
driver.find_element("xpath",'//*[@id="user-name"]').send_keys("Arsali")
driver.find_element("xpath",'//*[@id="password"]').send_keys("secret_sauce")
time.sleep(2)

#Klik button
elem = driver.find_element("xpath",'//*[@id="login-button"]')
elem.click()

time.sleep(1)

#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
teks_elemen = element.text

if element.text == "Epic sadface: Username and password do not match any user in this service":
    print("Validasi teks Gagal Login, berhasil")
else:
    print("Validasi teks gagal")

time.sleep(2)

