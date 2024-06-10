from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# inport jeda waktu
import time

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')



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





#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
teks_elemen = element.text

if element.text == "Products":
    print("Berhasil Login")
else:
    print("Test Case 1 Gagal")

#Pick Button Humbberger
dropdown_menu = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button')
time.sleep(2)
dropdown_menu.click()
time.sleep(2)

#Validasi Text Hamburger
element = driver.find_element(By.XPATH, '//*[@id="inventory_sidebar_link"]')
teks_elemen = element.text

if element.text == "All Items":
    print("Berhasil Klik humberger")
else:
    print("Klik humberger gagal")

#Klik button
elem = driver.find_element("xpath",'//*[@id="about_sidebar_link"]')
elem.click()

#Validasi Text
element = driver.find_element(By.XPATH, '//*[@id="__next"]/div[5]/div/div[1]/div[1]/h2')
teks_elemen = element.text

if element.text == "AUTOMATED TESTING & ERROR MONITORING SOLUTIONS":
    print("Berhasil Klik Side bar")
else:
    print("Klik side bar gagal")



driver.quit()