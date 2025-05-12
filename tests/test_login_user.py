import pytest
import allure

from playwright.sync_api import expect
from pages.home_page import Home
from data.test_data import Data
from utils.tools import take_screenshot
from pages.signup_login_page import SignUpLoginPage
from pages.header_page import Header

@allure.feature("User Login")
class TestLoginUser:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.header = Header(self.page)
        self.home = Home(self.page)
        self.signup = SignUpLoginPage(self.page)

    @allure.title("Login User with correct email and password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login_valid
    def test_login_user(self, test_setup, register_user):
        email, password, user_name = register_user

        with allure.step("Clear cookies and reload homepage"):
            self.page.context.clear_cookies()
            self.page.reload()

        take_screenshot(self.page, "user_logged_out")

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_signup_login_btn()

        with allure.step(f"Verify '{Data.login_form_text}' text is visible"):
            expect(self.signup.login_form_container).to_contain_text(Data.login_form_text)

        with allure.step(f"Fill login form with email: {email}, password: {password}"):
            self.signup.fill_in_login_form(email, password)
            self.signup.click_login_form_btn()

        with allure.step(f"Click 'Continue' and verify login as '{user_name}'"):
            expect(self.home.logged_in_as_text).to_have_text(Data.logged_in_as_text + user_name)

        with allure.step(f"Delete account and verify '{Data.account_deleted_text}' message"):
            self.home.click_delete_account_button()
            expect(self.home.account_deleted_text).to_have_text(Data.account_deleted_text)

    @allure.title("Login User with incorrect email and password")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login_invalid
    def test_login_invalid_user(self, test_setup):
        email = Data.get_random_email()
        password = Data.random_password()

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Click on 'Signup / Login' button"):
            self.header.click_signup_login_btn()

        with allure.step(f"Verify '{Data.login_form_text}' text is visible"):
            expect(self.signup.login_form_container).to_contain_text(Data.login_form_text)

        with allure.step(f"Fill login form with incorrect email: {email}, password: {password}"):
            self.signup.fill_in_login_form(email, password)
            self.signup.click_login_form_btn()

        with allure.step(f"Verify '{Data.incorrect_login_text}' text is visible"):
            expect(self.signup.login_form_error_text).to_have_text(Data.incorrect_login_text)

        take_screenshot(self.page, "login_error_text")