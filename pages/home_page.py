from playwright.sync_api import Page

class Home:
    def __init__(self, page: Page):
        self.page = page

        self.__items_container = self.page.locator('#slider+section .container')
        self.__logged_in_as_text = self.page.locator('a:has(i.fa-user)')
        self.__logout_btn = self.page.locator('a[href="/logout"]')
        self.__delete_account_button = self.page.locator('a[href="/delete_account"]')
        self.__account_deleted_text = self.page.locator('h2[data-qa="account-deleted"]')
        self.__footer_container = self.page.locator('.footer-widget')
        self.__subscription_email_input = self.page.locator('input[id="susbscribe_email"]')
        self.__subscribe_btn = self.page.locator('button[id="subscribe"]')
        self.__subscription_header_text = self.__footer_container.locator('h2')
        self.__success_subscribe_text = self.page.locator('#success-subscribe')

    @property
    def items_container(self):
        return self.__items_container

    @property
    def logged_in_as_text(self):
        return self.__logged_in_as_text

    @property
    def account_deleted_text(self):
        return self.__account_deleted_text

    @property
    def subscription_header_text(self):
        return self.__subscription_header_text

    @property
    def success_subscribe_text(self):
        return self.__success_subscribe_text

    def click_logout_btn(self):
        self.__logout_btn.click()

    def click_delete_account_button(self):
        self.__delete_account_button.click()

    def scroll_to_footer(self):
        self.__footer_container.scroll_into_view_if_needed()

    def fill_subscription_email_input(self, email):
        self.__subscription_email_input.fill(email)

    def click_subscribe_btn(self):
        self.__subscribe_btn.click()