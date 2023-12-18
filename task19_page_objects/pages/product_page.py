from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.product_first = None
        self.product_first_name = None
        self.value_count = 0
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # выставляем опции у товара, если они есть
    def set_option(self):
        if self.driver.find_element(By.ID, "box-product").find_element(By.CLASS_NAME, "title").text == 'Yellow Duck':
            self.driver.find_element(By.CSS_SELECTOR, "[name=buy_now_form]").find_element(By.CSS_SELECTOR, "[name='options[Size]']").send_keys("Small")

    # добавляем товар в корзину
    def click_add_product_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "[name=add_cart_product]").click()
        self.value_count += 1
        return self


    # ожидание появления элемента
    def wait_until_presence(self):
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='quantity' and text()='" + str(self.value_count) + "']")))
        return self

    # проверяем сколько товаров в корзине
    def check_count_products_in_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class=quantity]").text != "3"

    # переходим в корзину
    def click_to_cart(self):
        self.driver.find_element(By.XPATH, "//a[text()='Checkout »']").click()
        return self
