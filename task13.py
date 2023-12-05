import traceback
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# отделяем код товара
def code(string):
    product_code_old = string
    product_code = product_code_old.replace("[SKU: ", "").replace("]", "")
    return product_code


# функция добавления товаров в корзину
def add_to_cart():
    driver.get("http://localhost/litecart/en/")
    driver.find_element(By.CLASS_NAME, "product").click()
    value_count = int(driver.find_element(By.CSS_SELECTOR, "[class=quantity]").text)

    # проверяем наличие опций у товара
    try:
        driver.find_element(By.CSS_SELECTOR, "[name=buy_now_form]").find_element(By.CSS_SELECTOR, "[name='options[Size]']").send_keys("Small")
    except:
        pass

    # добавляем товар в корзину
    driver.find_element(By.CSS_SELECTOR, "[name=add_cart_product]").click()
    value_count += 1

    # ищем в корзине новое количество товаров
    try:
        driver.find_element(By.XPATH, "//span[@class='quantity' and text()='" + str(value_count) + "']")
    except NoSuchElementException:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        exit()
    return

# start
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
driver.get("http://localhost/litecart/en/")


# добавляем товары в корзину
while driver.find_element(By.CSS_SELECTOR, "[class=quantity]").text != "3":
    add_to_cart()

driver.find_element(By.XPATH, "//a[text()='Checkout »']").click()

# удаляем товары из корзины
while True:
    driver.refresh()

    product = driver.find_element(By.CSS_SELECTOR, "[class=viewport]").find_element(By.CSS_SELECTOR, "[class=item]")
    product_code = product.find_element(By.TAG_NAME, "span").text

    # находим элемент в нижней таблице, который должен удалиться
    element = driver.find_element(By.CSS_SELECTOR, "[class^='dataTable']").find_element(By.XPATH, "//td[@class='sku' and text()='" + code(product_code) + "']")

    # жмём кнопку "remove"
    product.find_element(By.CSS_SELECTOR, "[name=remove_cart_item]").click()

    wait = WebDriverWait(driver, 5)
    # ожидание исчезновения элемента из нижней таблицы
    wait.until(EC.staleness_of(element))

    # проверка на отсутствие элементов в корзине
    try:
        driver.find_element(By.XPATH, "//em[text()='There are no items in your cart.']")
        break
    except:
        pass

driver.quit()