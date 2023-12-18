from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.product_first = None
        self.product_first_name = None
        self.value_count = None
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # переходим на главную страницу
    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    # проверка нахождения на главной
    def is_on_main_page(self):
        return len(self.driver.find_elements(By.ID, "box-account-login")) > 0

    # переходим на страницу товара
    def click_on_product_page(self):
        self.product_first = self.driver.find_element(By.CLASS_NAME, "product")
        self.product_first_name = self.product_first.find_element(By.CSS_SELECTOR, "[class=name]").text
        self.product_first.click()
        self.value_count = int(self.driver.find_element(By.CSS_SELECTOR, "[class=quantity]").text)
        return self
