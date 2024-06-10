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

#Klik button add item
elem = driver.find_element("xpath",'//*[@id="add-to-cart-sauce-labs-backpack"]')
elem.click()

#Klik button shopping cart
elem = driver.find_element("xpath",'//*//*[@id="shopping_cart_container"]/a')
elem.click()

time.sleep(2)

#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
teks_elemen = element.text

if element.text == "Your Cart":
    print("Berhasil Menambahkan Item")
else:
    print("Gagal Menambahkan Item")

#Klik button Checkout
elem = driver.find_element("xpath",'//*[@id="checkout"]')
elem.click()

#Input Email dan Password
driver.find_element("xpath",'//*[@id="first-name"]').send_keys("Tugimin")
driver.find_element("xpath",'//*[@id="last-name"]').send_keys("firmansyah")
driver.find_element("xpath",'//*[@id="postal-code"]').send_keys("17324")
time.sleep(2)

#Klik button Continue
elem = driver.find_element("xpath",'//*[@id="continue"]')
elem.click()

#Klik button Continue
elem = driver.find_element("xpath",'//*[@id="finish"]')
elem.click()

#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
teks_elemen = element.text

if element.text == "Thank you for your order!":
    print("Order Berhasil")
else:
    print("Order Gagal")

driver.quit()
