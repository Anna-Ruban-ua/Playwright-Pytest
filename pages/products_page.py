from playwright.sync_api import Page

class Products:
    def __init__(self, page: Page):
        self.page = page

        self.__container = self.page.locator('.features_items')
        self.__container_text = self.__container.locator('h2.title.text-center')
        self.__view_first_product_button = self.page.locator('a[href="/product_details/1"]')
        self.__details_container = self.page.locator('.product-details')
        self.__product_name = self.__details_container.locator('h2')
        self.__product_category = self.__details_container.locator('p', has_text="Category")
        self.__product_price = self.__details_container.locator('span span')
        self.__product_availability = self.__details_container.locator('p', has_text="Availability")
        self.__product_condition = self.__details_container.locator('p', has_text="Condition")
        self.__product_brand = self.__details_container.locator('p', has_text="Brand")

    @property
    def container(self):
        return self.__container

    @property
    def container_text(self):
        return self.__container_text

    @property
    def details_container(self):
        return self.__details_container

    @property
    def product_name(self):
        return self.__product_name

    @property
    def product_category(self):
        return self.__product_category

    @property
    def product_price(self):
        return self.__product_price

    @property
    def product_availability(self):
        return self.__product_availability

    @property
    def product_condition(self):
        return self.__product_condition

    @property
    def product_brand(self):
        return self.__product_brand

    def click_on_first_product_button(self):
        self.__view_first_product_button.click()

    def get_product_details_text(self):
        def clean(text):
            return text.split(":", 1)[-1].strip()

        return (
            f"Name: {self.__product_name.inner_text()}\n"
            f"Category: {clean(self.__product_category.inner_text())}\n"
            f"Price: {self.__product_price.inner_text()}\n"
            f"Availability: {clean(self.__product_availability.inner_text())}\n"
            f"Condition: {clean(self.__product_condition.inner_text())}\n"
            f"Brand: {clean(self.__product_brand.inner_text())}"
        )