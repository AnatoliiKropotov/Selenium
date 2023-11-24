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

        # заходим в админку
        elem_login = driver.find_element(By.NAME, "username").send_keys("admin")
        elem_pass = driver.find_element(By.NAME, "password").send_keys("admin")
        elem_login_button = driver.find_element(By.NAME, "login").click()

        # список стран на странице
        list_countries_web = driver.find_elements(By.CLASS_NAME, "row")

        # список python для проверки сортировки
        list_check_sort = []

        for i in list_countries_web:
            country = i.find_element(By.TAG_NAME, "a")
            list_check_sort.append(country.text)

        list_after_sorted = sorted(list_check_sort)

        # проверка на сортировку стран
        if list_check_sort == list_after_sorted:
            print("Страны на странице отсортированы")
        else:
            print("Страны на странице НЕ отсортированы")

        # проверяем вложенные страны на сортировку
        for country in list_countries_web:
            list_td_tag = country.find_elements(By.TAG_NAME, "td")
            if int(list_td_tag[5].text) != 0:
                name_country = list_td_tag[4].text
                print(name_country)

                country_in = country.find_element(By.TAG_NAME, "a")
                print(country_in.get_attribute("outerHTML"))
                country_in.click()

                list_country_in = []
                dataTable = driver.find_element(By.CLASS_NAME, "dataTable")
                tr_tag_list = dataTable .find_elements(By.TAG_NAME, "tr")
                for tr in tr_tag_list:
                    td_tag_list = tr.find_elements(By.TAG_NAME, "input")
                    if len(td_tag_list) == 3:
                        list_country_in.append(td_tag_list[2].get_attribute("value"))
                list_country_in_sorted = sorted(list_country_in)
                if list_country_in == list_country_in_sorted:
                    print(f'Cписок стран внутри {name_country} отсортирован')
                else:
                    print(f'Cписок стран внутри {name_country} НЕ отсортирован')

                break



    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return


check_tab()
