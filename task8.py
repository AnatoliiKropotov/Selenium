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


# формирование списков стран для проверки
def check_sorted_countries():
    try:
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

        # логинимся
        elem_login = driver.find_element(By.NAME, "username").send_keys("admin")
        elem_pass = driver.find_element(By.NAME, "password").send_keys("admin")
        elem_login_button = driver.find_element(By.NAME, "login").click()

        place_where_check = driver.find_element(By.TAG_NAME, "h1").text

        # получаем список стран на странице
        list_countries_web = driver.find_elements(By.CLASS_NAME, "row")

        # формируем список python для проверки сортировки на странице countries
        list_on_page = []
        for i in list_countries_web:
            country = i.find_element(By.TAG_NAME, "a")
            list_on_page.append(country.text)

        # вызываем функцию проверки сортировки
        check_sorted_list(list_on_page, place_where_check)

        # проверяем вложенные страны на сортировку
        name_country_list = []
        stop = True
        while stop:
            list_countries_web = driver.find_elements(By.CLASS_NAME, "row")
            for country in list_countries_web:
                list_td_tag = country.find_elements(By.TAG_NAME, "td")
                if int(list_td_tag[5].text) != 0 and list_td_tag[4].text not in name_country_list:
                    name_country = list_td_tag[4].text
                    name_country_list.append(name_country)
                    country.find_element(By.TAG_NAME, "a").click()
                    list_country_in = []
                    tr_tag_list = driver.find_element(By.CLASS_NAME, "dataTable").find_elements(By.TAG_NAME, "tr")
                    for tr in tr_tag_list:
                        td_tag_list = tr.find_elements(By.TAG_NAME, "input")
                        if len(td_tag_list) == 3:
                            list_country_in.append(td_tag_list[2].get_attribute("value"))
                    check_sorted_list(list_country_in, name_country)
                    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
                    break

                elif len(list_countries_web) == list_countries_web.index(country) + 1:
                    stop = False
                    break

        driver.quit()
        return

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return


check_sorted_countries()
