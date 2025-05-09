from playwright.sync_api import Page

class Home:
    def __init__(self, page: Page):
        self.page = page

        self.__items_container = self.page.locator('#slider+section .container')
        self.__logged_in_as_text = self.page.locator('a:has(i.fa-user)')
        self.__delete_account_button = self.page.locator('a[href="/delete_account"]')
        self.__account_deleted_text = self.page.locator('h2[data-qa="account-deleted"]')

    @property
    def items_container(self):
        return self.__items_container

    @property
    def logged_in_as_text(self):
        return self.__logged_in_as_text

    @property
    def account_deleted_text(self):
        return self.__account_deleted_text

    def click_delete_account_button(self):
        self.__delete_account_button.click()