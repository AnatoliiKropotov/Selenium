import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def check_sticker():
    try:
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)

        driver.get("http://localhost/litecart/en/")

        product_bloks_list = driver.find_elements(By.CLASS_NAME, 'listing-wrapper.products')
        count_duck = 0
        count_sticker = 0
        for i in range(0, len(product_bloks_list)):
            products_list = product_bloks_list[i].find_elements(By.CLASS_NAME, "product")
            for j in range(0, len(products_list)):
                if len(products_list[j].find_elements(By.CSS_SELECTOR, "[class^='sticker']")) == 1:
                    count_sticker += 1
                count_duck += 1
        if count_duck == count_sticker:
            print("У каждого товара по одному стикеру: ", True)
        else:
            print("У каждого товара по одному стикеру: ", False)

        driver.quit()
        return

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return


check_sticker()