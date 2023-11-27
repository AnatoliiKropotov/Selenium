import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# проверка на сортировку списков
def check_sorted_list(list_on_page, parametr):
    list_after_sort = sorted(list_on_page)
    if list_on_page == list_after_sort:
        print(f"Страны внутри {parametr} расположены в алфавитном порядке")
    else:
        print(f"Страны внутри {parametr} НЕ расположены в алфавитном порядке")
    return


# составление списка геозон
def geo_zones():
    try:
        # задаём опции драйвера
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)

        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

        # логинимся
        elem_login = driver.find_element(By.NAME, "username").send_keys("admin")
        elem_pass = driver.find_element(By.NAME, "password").send_keys("admin")
        elem_login_button = driver.find_element(By.NAME, "login").click()

        list_zone = driver.find_elements(By.CLASS_NAME, "row")
        total_countries = len(list_zone)
        country_name = None
        count = 0
        while count != total_countries:

            # находим все страны с геозонами
            list_zone = driver.find_elements(By.CLASS_NAME, "row")
            total_countries = len(list_zone)

            # заходим на страницу страны
            for country in list_zone:
                button = country.find_element(By.TAG_NAME, "a")

                # проверка на уже проверенную страну
                if button.text == country_name:
                    continue
                country_name = button.text
                button.click()

                # собираем данные, какие геозоны выбраны
                table = driver.find_element(By.TAG_NAME, "table")

                list_selected_countries = []

                for row in table.find_elements(By.CSS_SELECTOR, "[selected=selected]"):
                    if row.get_attribute('data-phone-code') != "1":
                        list_selected_countries.append(row.text)
                check_sorted_list(list_selected_countries, country_name)

                driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
                count += 1
                break

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return


geo_zones()
