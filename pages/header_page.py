from playwright.sync_api import Page

class Header:
    def __init__(self, page: Page):
        self.page = page

        self.__home_btn = self.page.locator('a[href="/"]').nth(1)
        self.__products_btn = self.page.locator('a[href="/products/"]')
        self.__cart_btn = self.page.locator('a[href="/view_cart"]')
        self.__signup_login_btn = self.page.locator('a[href="/login"]')
        self.__test_cases_btn = self.page.locator('a[href="/test_cases"]')
        self.__api_testing_btn = self.page.locator('a[href="/api_list"]')
        self.__contact_us_btn = self.page.locator('a[href="/contact_us"]')

    def click_home_btn(self) -> None:
        self.__home_btn.click()

    def click_products_btn(self) -> None:
        self.__products_btn.click()

    def click_cart_btn(self) -> None:
        self.__cart_btn.click()

    def click_signup_login_btn(self) -> None:
        self.__signup_login_btn.click()

    def click_test_cases_btn(self) -> None:
        self.__test_cases_btn.click()

    def click_api_testing_btn(self) -> None:
        self.__api_testing_btn.click()

    def click_contact_us_btn(self) -> None:
        self.__contact_us_btn.click()