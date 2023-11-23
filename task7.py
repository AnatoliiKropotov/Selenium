from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# задаём опции открытия браузера
options = Options()

# на весь экран
options.add_argument("--start-maximized")

# создаём объект driver
driver = webdriver.Chrome(options=options)

# Метод get открывает сайт по ссылке
driver.get("http://localhost/litecart/en/")
time.sleep(5)

# список видимых кнопок
list_tabs = driver.find_elements(By.CLASS_NAME, "image")
print(len(list_tabs))
for i in list_tabs:
    print(i.get_attribute("outerHTML"))