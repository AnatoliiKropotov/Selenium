import time
import traceback
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def add_to_cart():
    driver.get("http://localhost/litecart/en/")
    driver.find_element(By.CLASS_NAME, "product").click()
    value_count = int(driver.find_element(By.CSS_SELECTOR, "[class=quantity]").text)
    print(value_count)

    # проверяем наличие опций у товара
    try:
        x = driver.find_element(By.CSS_SELECTOR, "[name=buy_now_form]").find_element(By.CSS_SELECTOR, "[class=options]")
        print(x.get_attribute("outerHTML"))
        driver.find_element(By.CSS_SELECTOR, "[name=buy_now_form]").find_element(By.CSS_SELECTOR, "[name='options[Size]']").send_keys("Small")
    except:
        print("У товара нет опций")

    # добавляем товар в корзину
    driver.find_element(By.CSS_SELECTOR, "[name=add_cart_product]").click()
    value_count += 1

    # ищем в корзине новое количество товаров
    try:
        driver.find_element(By.XPATH, "//span[@class='quantity' and text()='" + str(value_count) + "']")
        print(value_count)
    except NoSuchElementException:
        print("Возникла ошибка: ", traceback.format_exc())
        exit()

    return

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)
driver.get("http://localhost/litecart/en/")

while driver.find_element(By.CSS_SELECTOR, "[class=quantity]").text != "3":
    add_to_cart()
driver.find_element(By.XPATH, "//a[text()='Checkout »']").click()

# ищем кнопку "remove"
while True:
    try:
        x = driver.find_element(By.CSS_SELECTOR, "[class=dataTable.rounded-corners]").find_elements()

        driver.find_element(By.CSS_SELECTOR, "[name=remove_cart_item]").click()

    except:
        print("Все товары удалены")

time.sleep(3)
print("Дошли до 3х,конец")