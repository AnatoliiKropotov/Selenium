from selenium.task19_page_objects.application import Application

if __name__ == "__main__":
    app = Application()
    app.add_products_to_cart()
    app.delete_products_from_cart()
    app.quit()
