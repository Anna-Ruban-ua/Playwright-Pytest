import pytest
import allure
import random

from playwright.sync_api import expect
from pages.home_page import Home
from data.test_data import Data
from utils.tools import take_screenshot
from pages.header_page import Header
from pages.products_page import Products

@allure.feature("Products Page")
class TestProducts:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.header = Header(self.page)
        self.home = Home(self.page)
        self.products = Products(self.page)

    @allure.title("Verify All Products and product detail page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.product
    def test_products(self, test_setup):

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Click on 'Products' button"):
            self.header.click_products_btn()

        with allure.step(f"Verify '{Data.products_container_text}' text is visible"):
            expect(self.products.container_text).to_have_text(Data.products_container_text)

        with allure.step("Verify products is visible"):
            expect(self.products.container).to_be_visible()

        take_screenshot(self.page, "products")

        with allure.step("Click first 'View Product' button"):
            self.products.click_on_first_product_button()

        with allure.step("User is landed to product detail page"):
            expect(self.products.details_container).to_be_visible()

        with allure.step("Verify that detail detail is visible: product name, category, price, availability, condition, brand"):
            with allure.step(f"Verify product details:\n{self.products.get_product_details_text()}"):
                expect(self.products.product_name).to_be_visible()
                expect(self.products.product_category).to_be_visible()
                expect(self.products.product_price).to_be_visible()
                expect(self.products.product_availability).to_be_visible()
                expect(self.products.product_condition).to_be_visible()
                expect(self.products.product_brand).to_be_visible()

        take_screenshot(self.page, "product_details")

    @allure.title("Search Product")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.product
    @pytest.mark.search
    def test_products_search(self, test_setup):
        product_names = self.products.get_all_product_names()
        product_to_search = random.choice(product_names)

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Click on 'Products' button"):
            self.header.click_products_btn()

        with allure.step(f"Verify '{Data.products_container_text}' text is visible"):
            expect(self.products.container_text).to_have_text(Data.products_container_text)

        with allure.step("Verify products is visible"):
            expect(self.products.container).to_be_visible()

        take_screenshot(self.page, "products")

        with allure.step(f"Enter product name '{product_to_search}' in search input and click search button"):
            self.products.search_product(product_to_search)

        with allure.step(f"Verify '{Data.search_header_text}' text is visible"):
            expect(self.products.container_text).to_have_text(Data.search_header_text)

        with allure.step("Verify all the products related to search are visible"):
            results = self.products.search_result_titles
            count = results.count()
            for i in range(count):
                expect(results.nth(i)).to_contain_text(product_to_search)

        take_screenshot(self.page, "searched_products")