from playwright.sync_api import Page

class Cases:
    def __init__(self, page: Page):
        self.page = page

        self.__container = self.page.locator('#form div[class="container"]')

    @property
    def container(self):
        return self.__container