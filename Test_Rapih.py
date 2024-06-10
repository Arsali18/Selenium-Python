from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# inport jeda waktu
import time

driver = webdriver.Chrome()
driver.maximize_window()

# menambahkan alamat url
driver.get("https://simora.kemenag.go.id/login")
# tambahkan beberapa perintah pada element

#Input Email dan Password
driver.find_element("xpath",'/html/body/div/div/div/div/div[2]/form/input[2]').send_keys("Arsali")
driver.find_element("xpath",'/html/body/div/div/div/div/div[2]/form/input[3]').send_keys("Password")

time.sleep(2)

#Klik Button
elem = driver.find_element("xpath",'/html/body/div/div/div/div/div[2]/form/button')
elem.click()

#Validasi Text
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/span/strong')
teks_elemen = element.text

if element.text == "Identitas tersebut tidak cocok dengan data kami.":
    print("Validasi teks berhasil")
else:
    print("Validasi teks gagal")

time.sleep(2)

elem = driver.find_element(By.XPATH,"(//a[normalize-space()='Reset Password'])[1]").click()

# tambahkan jeda  detik sebelum keluar
time.sleep(2)


driver.quit()
