import time
import os
from datetime import date, timedelta
import string
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get("http://localhost/litecart/admin/")

driver.find_element(By.CSS_SELECTOR, '[name=username]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=password]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=login]').click()

driver.find_element(By.XPATH, '//span[text()="Catalog"]').click()
# .get_attribute("outerHTML"))
driver.find_element(By.XPATH, '//a[text()=" Add New Product"]').click()

# заполняем поля вкладки "General"
driver.find_element(By.XPATH, '//label[text()=" Enabled"]').click()

# поиск с начала строки по значению атрибута value
driver.find_element(By.CSS_SELECTOR, '[name^="name"]').send_keys("mattress")
driver.find_element(By.CSS_SELECTOR, '[name=code]').send_keys("55555")
driver.find_element(By.CSS_SELECTOR, '[value="1-3"]').click()

driver.find_element(By.CSS_SELECTOR, '[name=quantity]').clear()
driver.find_element(By.CSS_SELECTOR, '[name=quantity]').send_keys("10")

# получаем путь к картинке (она должна лежать в том же каталоге, что и данный скрипт)
absolute_path = os.getcwd()
absolute_path_image = os.getcwd() + "\\task12_image.jpg"
print(absolute_path_image)

# прописваем путь к картинке в DOM
driver.find_element(By.CSS_SELECTOR, '[name^="new_images"]').send_keys(absolute_path_image)

# заполняем дату
today = date.today()
from_date = today.strftime("%d.%m.%Y")
to_date = (today + timedelta(days=10)).strftime("%d.%m.%Y")
driver.find_element(By.CSS_SELECTOR, '[name=date_valid_from]').send_keys(from_date)
driver.find_element(By.CSS_SELECTOR, '[name=date_valid_to]').send_keys(to_date)
# driver.find_element(By.XPATH, '//tr//label[text()="Unisex"]').click()

# переходим а вкладку "Information"
driver.find_element(By.XPATH, '//a[text()="Information"]').click()
driver.find_element(By.CSS_SELECTOR, "[name=manufacturer_id]").find_element(By.XPATH, 'option[text()="ACME Corp."]').click()

time.sleep(3)
exit()

driver.quit()
