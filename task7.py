import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def check_duck():
    try:
        # задаём опции драйвера
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)

        driver.get("http://localhost/litecart/en/")

        # находим всех уток
        list_tabs = driver.find_elements(By.CLASS_NAME, "hover-light")
        count_duck = len(list_tabs)
        print(count_duck)

        count_one_sticker_duck = 0
        for i in list_tabs:
            list_elements = i.find_elements(By.TAG_NAME, "div")

            # проверяем что существует один стикер на каждой утке
            if len(list_elements) == 1:
                count_one_sticker_duck += 1

        # условие на вывод
        if count_duck == count_one_sticker_duck:
            print(f"У каждой утки по одному нужному стикеру. Всего уток {count_duck}")
        else:
            print("Не у каждой утки нужное количество стикеров")
        driver.quit()
        return

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return


check_duck()
