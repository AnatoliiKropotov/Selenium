import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get("http://localhost/litecart/admin/")

driver.find_element(By.CSS_SELECTOR, '[name=username]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=password]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=login]').click()

driver.find_element(By.XPATH, '//span[text()="Catalog"]').click()
driver.find_element(By.XPATH, '//a[text()="Rubber Ducks"]').click()
driver.find_element(By.LINK_TEXT, "Subcategory").click()

x = driver.find_elements(By.XPATH, '//a[contains(text(), "Duck") and not(contains(text(), "Ducks"))]')
count = 0
for i in range(0, len(x)):
    x[i].click()

    # выводим логи если массив не пустой
    logs = driver.get_log("browser")
    if logs:
        for log in logs:
            print(log)

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=2")
    x = driver.find_elements(By.XPATH, '//a[contains(text(), "Duck") and not(contains(text(), "Ducks"))]')
    count += 1

driver.quit()