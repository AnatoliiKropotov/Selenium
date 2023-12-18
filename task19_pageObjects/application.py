from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class Application:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=self.options)
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    # добавляем 3 товара в корзину
    def add_products_to_cart(self):
        while True:
            self.main_page.open()
            self.main_page.click_on_product_page()
            self.product_page.set_option()
            self.product_page.click_add_product_to_cart()
            self.product_page.wait_until_presence()
            if self.product_page.check_count_products_in_cart():
                continue
            else:
                break
        self.product_page.click_to_cart()

    # удаляем все товары из корзины
    def delete_products_from_cart(self):
        while True:
            self.cart_page.refresh_page()
            self.cart_page.catch_product_code()
            self.cart_page.click_delete_product()
            self.cart_page.wait_until_stale()
            if self.cart_page.check_empty_cart():
                break

    def quit(self):
        self.driver.quit()