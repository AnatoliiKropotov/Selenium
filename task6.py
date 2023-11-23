import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
        driver.get("http://localhost/litecart/admin")

        # заходим в админку
        elem_login = driver.find_element(By.NAME, "username").send_keys("admin")
        elem_pass = driver.find_element(By.NAME, "password").send_keys("admin")
        elem_login_button = driver.find_element(By.NAME, "login").click()

        # список видимых кнопок
        list_tabs = driver.find_elements(By.CLASS_NAME, "name")

        # кликаем на все нопки слева
        lst_h1 = []
        index_next_button = 0
        while True:
            lst_tags = []
            button = list_tabs[index_next_button]
            text_button = button.text
            button.click()
            print(f"Нажали на кнопку {text_button}")
            list_tabs = driver.find_elements(By.CLASS_NAME, "name")

            # Проверяем наличие заголовка
            if driver.find_elements(By.TAG_NAME, "h1"):
                lst_h1.append((text_button, True))
            else:
                lst_h1.append((text_button, False))

            # составляем список имён кнопок
            for i in list_tabs:
                lst_tags.append(i.text)

            # проверка на одинаковые имена кнопок
            if index_next_button == lst_tags.index(text_button) + 1:
                index_next_button += 1
            else:
                index_next_button = lst_tags.index(text_button) + 1

            # проверка на конец списка кнопок
            if index_next_button == len(list_tabs):
                driver.quit()

                print("Наличие заголовка:")
                for i in lst_h1:
                    print(i)
                return

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return

check_tab()
