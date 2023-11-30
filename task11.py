import string
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def generator(parameter):
    # Генерируем firstname, lastname, adress
    if parameter == 1:
        str_ = ''.join(random.choice(string.ascii_uppercase if i == 0 else string.ascii_lowercase)
                       for i in range(0, random.randint(3, 10)))
        return str_

    # postcode
    elif parameter == 2:
        postcode = ''.join(random.choice(string.digits) for i in range(0, 5))
        return postcode

    # phone
    elif parameter == 3:
        phone = "+1"
        for i in range(0, 10):
            phone += str(random.randint(0, 9))
        return phone

    # email
    elif parameter == 4:
        email = ""
        for i in range(0, 10):
            if i == 5:
                email += "@"
            else:
                email += str(random.choice(string.ascii_lowercase + string.digits))
        print("email: ", email)
        return email

    # password
    elif parameter == 5:
        password = ''.join(random.choice(string.ascii_lowercase)
                           for i in range(0, random.randint(3, 10)))
        print("password: ", password)
        return password


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get("http://localhost/litecart/en/")

# переходим на страницу регистрации
driver.find_element(By.XPATH, '//a[text()="New customers click here"]').click()

# создаём аккаунт
driver.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys(generator(1))
driver.find_element(By.CSS_SELECTOR, '[name=lastname]').send_keys(generator(1))
driver.find_element(By.CSS_SELECTOR, '[name=address1]').send_keys(generator(1))
driver.find_element(By.CSS_SELECTOR, '[name=postcode]').send_keys(generator(2))
driver.find_element(By.CSS_SELECTOR, '[name=city]').send_keys(generator(1))

# выбираем страну
driver.find_element(By.CLASS_NAME, 'select2-selection__arrow').click()
driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys('United States')
driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//select[@name="zone_code"]').find_element(By.CSS_SELECTOR, '[value=KY]').click()
driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys(generator(3))
email = generator(4)
driver.find_element(By.CSS_SELECTOR, '[name=email]').send_keys(email)

password = generator(5)
driver.find_element(By.CSS_SELECTOR, '[name=password]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[name=confirmed_password]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[name=create_account]').click()

# logout
driver.find_element(By.XPATH, '//a[text()="Logout"]').click()

# login
driver.find_element(By.CSS_SELECTOR, '[name=email]').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '[name=password]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[name=login]').click()

# logout
driver.find_element(By.XPATH, '//a[text()="Logout"]').click()

driver.quit()