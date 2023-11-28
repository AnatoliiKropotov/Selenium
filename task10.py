import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# составление списка геозон
def func():
    try:
        # задаём опции драйвера
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)

        driver.get("http://localhost/litecart/en/")

        block_campaigns = driver.find_element(By.ID, "box-campaigns")
        # print(block_campaigns.get_attribute("outerHTML"))

        # так как нам нужен первый товар, используем find_element
        duck_name = block_campaigns.find_element(By.CLASS_NAME, "name").text
        manufacture_name = block_campaigns.find_element(By.CLASS_NAME, "manufacturer").text

        regular_price = block_campaigns.find_element(By.CLASS_NAME, "regular-price").text
        regular_price_color = block_campaigns.find_element(By.CLASS_NAME, "regular-price").value_of_css_property(
            "color")
        regular_price_style = block_campaigns.find_element(By.CLASS_NAME, "regular-price").tag_name

        regular_price_height = block_campaigns.find_element(By.CLASS_NAME, "regular-price").get_property("offsetHeight")
        regular_price_width = block_campaigns.find_element(By.CLASS_NAME, "regular-price").get_property(
            "offsetWidth")

        campaign_price = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").text
        campaign_price_color = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").value_of_css_property(
            "color")
        campaign_price_style = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").tag_name

        campaign_price_height = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").get_property(
            "offsetHeight")
        campaign_price_width = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").get_property(
            "offsetWidth")

        main_page_values = (duck_name, manufacture_name, regular_price, regular_price_color, regular_price_style,
                            campaign_price, campaign_price_color, campaign_price_style, regular_price_height,
                            regular_price_width, campaign_price_height, campaign_price_width)
        print(main_page_values)
        # print(duck_name)
        # print(manufacture_name)
        # print(regular_price)
        # print(regular_price_color)
        # print(regular_price_style)
        # print(campaign_price)
        # print(campaign_price_color)
        # print(campaign_price_style)
        # print(regular_price_height)
        # print(regular_price_width)
        # print(campaign_price_height)
        # print(campaign_price_width)


        # переходим внуть товара
        block_campaigns.find_element(By.CLASS_NAME, "listing-wrapper.products").find_element(By.TAG_NAME, 'a').click()

        block_campaigns = driver.find_element(By.ID, "box-product")
        print(block_campaigns.get_attribute("outerHTML"))
        regular_price_inner = block_campaigns.find_element(By.CLASS_NAME, "regular-price").text
        campaign_price_inner = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").text
        print(regular_price_inner)
        print(campaign_price_inner)

        # print(block_campaigns.get_attribute("outerHTML"))


        return

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return


func()
