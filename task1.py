import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# задаём опции открытия браузера
options = Options()
# на весь экран
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

time.sleep(3)

# Метод get открыает сайт по ссылке
driver.get("https://www.google.com/")
time.sleep(3)

driver.quit()
