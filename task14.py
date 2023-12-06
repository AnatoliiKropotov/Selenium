import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get("http://localhost/litecart/admin/")

driver.find_element(By.CSS_SELECTOR, '[name=username]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=password]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[name=login]').click()

driver.find_element(By.XPATH, '//span[text()="Countries"]').click()

# получаем список стран на странице
list_countries_web = driver.find_elements(By.CLASS_NAME, "row")
list_on_page = []
for i in list_countries_web:
    country = i.find_element(By.TAG_NAME, "a")
    list_on_page.append(country.text)

# выбираем страну для проверки
country_check = random.choice(list_on_page)

# заходим в эту страну
driver.find_element(By.XPATH, "//a[text()='" + country_check + "']").click()

list_links = driver.find_elements(By.XPATH, "//td/a[@target='_blank']")
main_window = driver.current_window_handle

# прокликиваем ссылки
for i in range(0, len(list_links)):
    # список открытых окон
    all_handles = driver.window_handles
    list_links[i].click()

    # ожидание открытия нового окна
    wait = WebDriverWait(driver, 5)
    wait.until(EC.new_window_is_opened(all_handles))

    # находим handle нового окна
    all_window_handles = driver.window_handles
    all_window_handles.remove(main_window)
    new_window = all_window_handles[0]

    # захватываем новое окно
    driver.switch_to.window(new_window)

    # закрываем новое окно
    driver.close()

    # переключаемся на main окно
    driver.switch_to.window(main_window)

driver.quit()