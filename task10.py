import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# а) на главной странице и на странице товара совпадает текст названия товара
def check_name(main_page_name, inner_page_name):
    if main_page_name == inner_page_name:
        print("Название товара на главной и внутри совпадает: ", True)
    else:
        print("Название товара на главной и внутри совпадает: ", False)


# б) на главной странице и на странице товара совпадают цены (обычная и акционная)
def check_price(main_page_price, inner_page_price, type_price):
    if main_page_price == inner_page_price:
        print(f"Цена товара {type_price} на главной и внутри совпадает: ", True)
    else:
        print(f"Цена товара {type_price} на главной и внутри cовпадает: ", False)


# в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой,
# у которого в RGBa представлении одинаковые значения для каналов R, G и B)
def check_price_style_regular(regular_price_color, regular_price_style, page):
    if regular_price_color[0] == regular_price_color[1] == regular_price_color[2] and regular_price_style == 's':
        print(f"{page}: цвет обычной цены серый, стиль перечёркнутый: ", True)
    else:
        print(f"{page}: цвет обычной цены серый, стиль перечёркнутый: ", False)


# г) акционная цена жирная и красная (можно считать, что "красный" цвет это такой,
# у которого в RGBa представлении каналы G и B имеют нулевые значения)
def check_price_style_campaign(campaign_price_color, campaign_price_style, page):
    if campaign_price_color[1] == campaign_price_color[2] == 0 and campaign_price_style == 'strong':
        print(f"{page}: цвет акционной цены красный, стиль жирный: ", True)
    else:
        print(f"{page}: цвет обычной цены красный, стиль жирный: ", False)


# д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
def check_price_size(regular_price_height, regular_price_width, campaign_price_height, campaign_price_width, page):
    if (campaign_price_height >= regular_price_height and campaign_price_width > regular_price_width or
            campaign_price_height > regular_price_height and campaign_price_width >= regular_price_width):
        print(f"{page}: акционная цена крупнее, чем обычная:", True)
    else:
        print(f"{page}: акционная цена крупнее, чем обычная:", False)


# переводим цвет в кортеж
def color_to_tuple(color):
    color_str = color.replace("rgba", "").strip("()")
    color = tuple(int(item) for item in color_str.split(','))
    return color


# получения значений товара
def main():
    try:
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)

        driver.get("http://localhost/litecart/en/")

        block_campaigns = driver.find_element(By.ID, "box-campaigns")

        # так как нам нужен первый товар, используем find_element
        duck_name = block_campaigns.find_element(By.CLASS_NAME, "name").text
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

        # для наглядности выводим найденные параметры
        main_page_values = (duck_name, regular_price, regular_price_color, regular_price_style,
                            campaign_price, campaign_price_color, campaign_price_style, regular_price_height,
                            regular_price_width, campaign_price_height, campaign_price_width)
        print(main_page_values)

        # переходим внуть товара
        block_campaigns.find_element(By.CLASS_NAME, "listing-wrapper.products").find_element(By.TAG_NAME, 'a').click()

        block_campaigns = driver.find_element(By.ID, "box-product")

        duck_name_inner = block_campaigns.find_element(By.CLASS_NAME, "title").text
        regular_price_inner = block_campaigns.find_element(By.CLASS_NAME, "regular-price").text
        regular_price_color_inner = block_campaigns.find_element(By.CLASS_NAME, "regular-price").value_of_css_property(
            "color")
        regular_price_style_inner = block_campaigns.find_element(By.CLASS_NAME, "regular-price").tag_name
        regular_price_height_inner = block_campaigns.find_element(By.CLASS_NAME, "regular-price").get_property(
            "offsetHeight")
        regular_price_width_inner = block_campaigns.find_element(By.CLASS_NAME, "regular-price").get_property(
            "offsetWidth")
        campaign_price_inner = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").text
        campaign_price_color_inner = block_campaigns.find_element(By.CLASS_NAME,
                                                                  "campaign-price").value_of_css_property(
            "color")
        campaign_price_style_inner = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").tag_name
        campaign_price_height_inner = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").get_property(
            "offsetHeight")
        campaign_price_width_inner = block_campaigns.find_element(By.CLASS_NAME, "campaign-price").get_property(
            "offsetWidth")

        # для наглядности выводим найденные параметры
        values_inner = (duck_name_inner, regular_price_inner, regular_price_color_inner, regular_price_style_inner,
                        campaign_price_inner, campaign_price_color_inner, campaign_price_style_inner,
                        regular_price_height_inner, regular_price_width_inner, campaign_price_height_inner,
                        campaign_price_width_inner)
        print(values_inner)

        # делаем проверки
        # название
        check_name(duck_name, duck_name_inner)
        # значение цены
        type_price = "обычная"
        check_price(regular_price, regular_price_inner, type_price)
        type_price = "акционная"
        check_price(campaign_price, campaign_price_inner, type_price)
        # цвет, стиль, размер цены
        page = "Главная страница"
        check_price_style_regular(color_to_tuple(regular_price_color), regular_price_style, page)
        check_price_style_campaign(color_to_tuple(campaign_price_color), campaign_price_style, page)
        check_price_size(regular_price_height, regular_price_width, campaign_price_height, campaign_price_width, page)
        page = "Карточка товара"
        check_price_style_regular(color_to_tuple(regular_price_color_inner), regular_price_style_inner, page)
        check_price_style_campaign(color_to_tuple(campaign_price_color_inner), campaign_price_style_inner, page)
        check_price_size(regular_price_height_inner, regular_price_width_inner, campaign_price_height_inner,
                         campaign_price_width_inner, page)

        return

    except Exception:
        print("Возникла ошибка: ", traceback.format_exc())
        driver.quit()
        return


main()
