import os
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get("http://localhost/litecart/admin/")

driver.find_element(By.CSS_SELECTOR, '[name=username]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=password]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=login]').click()

driver.find_element(By.XPATH, '//span[text()="Catalog"]').click()
driver.find_element(By.XPATH, '//a[text()=" Add New Product"]').click()

# заполняем поля вкладки "General"
driver.find_element(By.XPATH, '//label[text()=" Enabled"]').click()
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

# заполняем вкладку "Information"
driver.find_element(By.XPATH, '//a[text()="Information"]').click()
driver.find_element(By.CSS_SELECTOR, "[name=manufacturer_id]").find_element(By.XPATH, 'option[text()="ACME Corp."]').click()
driver.find_element(By.CSS_SELECTOR, '[name="short_description[en]"]').send_keys('This is a wonderful mattress')
driver.find_element(By.CSS_SELECTOR, '[class="trumbowyg-editor"]').send_keys(
    'This is a wonderful mattress. It will keep your spine in excellent tone. Your back will thank you!')

# заполняем вкладку "Prices"
driver.find_element(By.XPATH, '//a[text()="Prices"]').click()
driver.find_element(By.CSS_SELECTOR, '[name=purchase_price]').clear()
driver.find_element(By.CSS_SELECTOR, '[name=purchase_price]').send_keys("100")
driver.find_element(By.CSS_SELECTOR, '[name=purchase_price_currency_code]').send_keys("USD")
driver.find_element(By.CSS_SELECTOR, '[name="prices[USD]"]').send_keys("150")

# сохраняем товар
driver.find_element(By.CSS_SELECTOR, '[name="save"]').click()

# проверяем что товар появился в магазине
if driver.find_elements(By.XPATH, '//a[text()="mattress"]'):
    print("Проверка наличия товара в каталоге: ", True)
else:
    print("Проверка наличия товара в каталоге: ", False)

driver.quit()
