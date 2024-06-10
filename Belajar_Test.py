from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://simora.kemenag.go.id/login")

driver.find_element("xpath",'/html/body/div/div/div/div/div[2]/form/input[2]').send_keys("Arsali")
driver.find_element("xpath",'/html/body/div/div/div/div/div[2]/form/input[3]').send_keys("Password")

#button = wait.until(EC.element_to_be_clickable((By.XPATH, "b/html/body/div/div/div/div/div[2]/form/button"))).button.click()
elem = driver.find_element("xpath",'/html/body/div/div/div/div/div[2]/form/button')
elem.click()

# Cari element dengan id "myElement"
element = driver.find_element("xpath",'/html/body/div/div/div/div/div[2]/form/span/strong')
element = driver.find_element("xpath","(//a[normalize-space()='Reset Password'])[1]")
elem.click()

# Validasi text element
if element.text == "Identitas tersebut tidak cocok dengan data kami.":
    print("Validasi teks berhasil")
else:
    print("Validasi teks gagal")

elem = driver.find_element(By.XPATH,"(//a[normalize-space()='Reset Password'])[1]").click()


#element = driver.find_element("link_text",'Reset Password')
#element.click()
