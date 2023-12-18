from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # отделяем код товара
    def code(self):
        self.product_code = self.product_code.replace("[SKU: ", "").replace("]", "")
        return self.product_code

    # обновляем страницу
    def refresh_page(self):
        self.driver.refresh()
        return self

    # захватываем код удаляемого товара
    def catch_product_code(self):
        self.product = self.driver.find_element(By.CSS_SELECTOR, "[class=viewport]").find_element(By.CSS_SELECTOR, "[class=item]")
        self.product_code = self.product.find_element(By.TAG_NAME, "span").text

    # находим элемент в нижней таблице, который должен удалиться
    def click_delete_product(self):
        self.element = self.driver.find_element(By.CSS_SELECTOR, "[class^='dataTable']").find_element(By.XPATH,"//td[@class='sku' and text()='" + self.code() + "']")
        self.product.find_element(By.CSS_SELECTOR, "[name=remove_cart_item]").click()

    # ожидание исчезновения элемента из нижней таблицы
    def wait_until_stale(self):
        self.wait.until(EC.staleness_of(self.element))

    # проверка на отсутствие элементов в корзине
    def check_empty_cart(self):
        try:
            self.driver.find_element(By.XPATH, "//em[text()='There are no items in your cart.']")
            return True
        except:
            return False
