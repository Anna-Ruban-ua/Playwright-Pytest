import pytest
import allure

from playwright.sync_api import expect
from pages.home_page import Home
from data.test_data import Data
from utils.tools import take_screenshot
from pages.header_page import Header
from pages.contact_us_page import ContactUs

@allure.feature("Contact Us Form")
class TestContactUs:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.header = Header(self.page)
        self.home = Home(self.page)
        self.contact = ContactUs(self.page)

    @allure.title("Contact Us Form")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.form
    @pytest.mark.contact
    def test_contact_us(self, test_setup):
        name = Data.random_username()
        email = Data.get_random_email()
        subject = Data.random_subject()
        message = Data.random_message()

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Click on 'Contact Us' button"):
            self.header.click_contact_us_btn()

        with allure.step(f"Verify '{Data.contact_us_verification_text}' text is visible"):
            expect(self.contact.verif_text).to_have_text(Data.contact_us_verification_text)

        with allure.step(f"Fill contact us form with name: {name}, email: {email}"):
            self.contact.fill_contact_us_form(name, email, subject, message)

        with allure.step("Upload file"):
            self.contact.upload_temp_file()

        take_screenshot(self.page, "filled_form")

        with allure.step("Click 'Submit' button"):
            self.contact.click_submit_button_and_accept_alert()

        take_screenshot(self.page, "filled")

        with allure.step(f"Verify '{Data.contact_us_success_text}' text is visible"):
            expect(self.contact.success_text).to_have_text(Data.contact_us_success_text)

        with allure.step("Click 'Home' button and verify homepage is visible"):
            self.contact.click_home_btn()
            expect(self.home.items_container).to_be_visible()
