import pytest
import allure
from playwright.sync_api import expect

from pages.header_page import Header
from pages.home_page import Home
from pages.signup_login_page import SignUpLoginPage
from data.test_data import Data
from utils.tools import take_screenshot

@allure.feature("User Registration")
@allure.severity(allure.severity_level.CRITICAL)
class TestRegisterUser:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.header = Header(self.page)
        self.home = Home(self.page)
        self.signup = SignUpLoginPage(self.page)

    @allure.title("Register and delete user")
    @pytest.mark.one
    def test_register_user(self, test_setup):
        user_name = Data.random_username()
        email = Data.get_random_email()
        password = Data.random_password()
        day, month, year = Data.random_birth_date()

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_signup_login_btn()

        with allure.step(f"Verify '{Data.signup_form_text}' text is visible"):
            expect(self.signup.signup_form_container).to_contain_text(Data.signup_form_text)

        with allure.step(f"Fill signup form with username: {user_name}, email: {email}"):
            self.signup.fill_in_signup_form(user_name, email)
            self.signup.click_signup_form_btn()

        with allure.step(f"Verify '{Data.signup_account_info_text}' text is visible"):
            expect(self.signup.signup_account_info_text).to_have_text(Data.signup_account_info_text)

        with allure.step("Fill account information"):
            self.signup.fill_in_account_info(password)
            self.signup.select_birth_date(day, month, year)
            self.signup.set_checkboxes()

        with allure.step("Fill address information"):
            self.signup.fill_address_info(*Data.get_full_address_data())

        take_screenshot(self.page, "registered_user_data")

        with allure.step(f"Click 'Create Account' and verify '{Data.signed_up_account_info_text}'"):
            self.signup.click_create_account_button()
            expect(self.signup.signed_up_account_info_text).to_have_text(Data.signed_up_account_info_text)

        with allure.step(f"Click 'Continue' and verify login as '{user_name}'"):
            self.signup.click_continue_button()
            expect(self.home.logged_in_as_text).to_have_text(Data.logged_in_as_text + user_name)

        with allure.step(f"Delete account and verify '{Data.account_deleted_text}' message"):
            self.home.click_delete_account_button()
            expect(self.home.account_deleted_text).to_have_text(Data.account_deleted_text)

        take_screenshot(self.page, "account_deleted")