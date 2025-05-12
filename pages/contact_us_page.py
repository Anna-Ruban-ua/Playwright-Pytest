from playwright.sync_api import Page
import tempfile
import os

class ContactUs:
    def __init__(self, page: Page):
        self.page = page

        self.__contact_us_container = self.page.locator('.contact-form')
        self.__verif_text = self.__contact_us_container.locator('h2')
        self.__name_input = self.__contact_us_container.locator('input[name="name"]')
        self.__email_input = self.__contact_us_container.locator('input[type="email"]')
        self.__subject_input = self.__contact_us_container.locator('input[name="subject"]')
        self.__text_area_input = self.__contact_us_container.locator('textarea')
        self.__upload_file_button = self.__contact_us_container.locator('input[type="file"]')
        self.__submit_button = self.__contact_us_container.locator('input[type="submit"]')
        self.__success_text = self.page.locator('div[class="status alert alert-success"]')
        self.__home_btn = self.page.locator('.contact-form a[href="/"]')

    @property
    def verif_text(self):
        return self.__verif_text

    @property
    def success_text(self):
        return self.__success_text

    def fill_contact_us_form(self, user_name: str, email: str, subject: str, message: str) -> None:
        self.__name_input.fill(user_name)
        self.__email_input.fill(email)
        self.__subject_input.fill(subject)
        self.__text_area_input.fill(message)

    def click_submit_button_and_accept_alert(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.__submit_button.click()

    def click_home_btn(self):
        self.__home_btn.click()

    def upload_temp_file(self) -> None:
        import allure
        with allure.step("Create temp file, upload it and delete after"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
                tmp.write(b"This is a test file for upload.")
                tmp_path = tmp.name

            self.__upload_file_button.set_input_files(tmp_path)

            if os.path.exists(tmp_path):
                os.remove(tmp_path)