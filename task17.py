import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(1)

driver.get("http://localhost/litecart/admin/")

driver.find_element(By.CSS_SELECTOR, '[name=username]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=password]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=login]').click()

driver.find_element(By.XPATH, '//span[text()="Catalog"]').click()

driver.find_element(By.XPATH, '//a[text()="Rubber Ducks"]').click()

# text_colspan = driver.find_element(By.CSS_SELECTOR, '[colspan="5"]').text


# x = driver.find_elements(By.XPATH, '//a[contains(text(), "Duck") and not(contains(text(), "Ducks"))]')
# print(len(x))
# len_list = len(x)
# for i in x:
#     print(i.get_attribute('outerHTML'))

string_colspan = driver.find_element(By.CSS_SELECTOR, '[colspan="5"]').text
list_strings = string_colspan.split('|')
count_categories = int(list_strings[0].replace('Categories: ',''))
count_products = int(list_strings[1].replace('Products: ',''))
print("count_products: ", count_products)

category_number = 1
while category_number <= count_categories:
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=" + str(category_number))
    if category_number != 1:
        driver.find_element(By.LINK_TEXT, "http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=" + str(category_number)).click()
        list_strings= driver.find_element(By.CSS_SELECTOR, '[colspan="5"]').text.split('|')
        count_products_new = int(list_strings[1].replace('Products: ', ''))
        print("count_products_new:", count_products_new)
        if count_products_new - count_products == 0:
            category_number += 1
            continue
        else:
            count_products = count_products_new - count_products


    count = 1
    while count != count_products:
        print('1')
        print(driver.find_element(By.LINK_TEXT, "http://localhost/litecart/admin/?app=catalog&doc=edit_product&category_id=" + str(category_number) + "&product_id=" + str(count)))
        driver.find_element(By.LINK_TEXT, "http://localhost/litecart/admin/?app=catalog&doc=edit_product&category_id=" + str(category_number) + "&product_id=" + str(count)).click()
        logs = driver.get_log("browser")

        # выводим логи если массив не пустой
        if logs:
            for log in logs:
                print(log)

        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=" + str(category_number))
        # x = driver.find_elements(By.XPATH, '//a[contains(text(), "Duck") and not(contains(text(), "Ducks"))]')
        count += 1
    category_number += 1

driver.quit()