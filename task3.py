import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def login_admin():
    try:
        # задаём опции открытия браузера
        options = Options()

        # на весь экран
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

        # Метод get открыdает сайт по ссылке
        driver.get("http://localhost/litecart/admin")

        # заполняем форму с логином/паролем, кликаем по кнопке "логин"
        elem_login = driver.find_element(By.NAME, "username").send_keys("admin")
        elem_pass = driver.find_element(By.NAME, "password").send_keys("admin")
        elem_login_button = driver.find_element(By.NAME, "login").click()

        driver.quit()

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()

login_admin()
