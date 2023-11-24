import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def check_tab():
    try:
        # задаём опции открытия браузера
        options = Options()

        # на весь экран
        options.add_argument("--start-maximized")

        # создаём объект driver
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)

        # Метод get открывает сайт по ссылке
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

        time.sleep(5)

        # заходим в админку
        elem_login = driver.find_element(By.NAME, "username").send_keys("admin")
        elem_pass = driver.find_element(By.NAME, "password").send_keys("admin")
        elem_login_button = driver.find_element(By.NAME, "login").click()

        time.sleep(5)

        # список стран на странице
        list_countries_web = driver.find_elements(By.CLASS_NAME, "row")

        # список python для проверки сортировки
        list_check_sort = []

        for i in list_countries_web:
            country = i.find_element(By.TAG_NAME, "a")
            # print(countries.get_attribute("outerHTML"))
            # print(country.text)
            list_check_sort.append(country.text)

        list_after_sorted = sorted(list_check_sort)

        # проверка на сортировку стран
        if list_check_sort == list_after_sorted:
            print("Страны на странице отсортированы")
        else:
            print("Страны на странице НЕ отсортированы")

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return

check_tab()
