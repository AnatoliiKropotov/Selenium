import string
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты
# (чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих
# запусках того же самого сценария)
# 2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
# 3) повторный вход в только что созданную учётную запись,
# 4) и ещё раз выход.
# В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.

def generator(parameter):
    # Генерируем firstname, lastname, adress
    if parameter == 1:
        str_ = ""
        for i in range(0, random.randint(3, 10)):
            if i == 0:
                str_ += random.choice(string.ascii_uppercase)
            else:
                str_ += random.choice(string.ascii_lowercase)
        print(str_)
        return str_


    elif parameter == 2:
        pass



options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get("http://localhost/litecart/en/")

# переходим на страницу регистрации
driver.find_element(By.XPATH, '//a[text()="New customers click here"]').click()

driver.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys(generator(1))
driver.find_element(By.CSS_SELECTOR, '[name=lastname]').send_keys(generator(1))
driver.find_element(By.CSS_SELECTOR, '[name=address1]').send_keys(generator(1))
driver.find_element(By.CSS_SELECTOR, '[name=address1]').send_keys(generator(2))
# print(firstname.get_attribute("outerHTML"))
time.sleep(3)
