import allure
from playwright.sync_api import expect

from pages.header_page import Header
from pages.home_page import Home
from pages.signup_login_page import SignUpLoginPage
from data.test_data import Data
from utils.tools import take_screenshot


def register_user(page):
    header = Header(page)
    home = Home(page)
    signup = SignUpLoginPage(page)

    user_name = Data.random_username()
    email = Data.get_random_email()
    password = Data.random_password()
    day, month, year = Data.random_birth_date()

    with allure.step("Verify homepage is visible"):
        expect(home.items_container).to_be_visible()

    with allure.step("Click on 'Signup / Login' button"):
        header.click_signup_login_btn()

    with allure.step(f"Verify '{Data.signup_form_text}' text is visible"):
        expect(signup.signup_form_container).to_contain_text(Data.signup_form_text)

    with allure.step(f"Fill signup form with username: {user_name}, email: {email}"):
        signup.fill_in_signup_form(user_name, email)
        signup.click_signup_form_btn()

    with allure.step(f"Verify '{Data.signup_account_info_text}' text is visible"):
        expect(signup.signup_account_info_text).to_have_text(Data.signup_account_info_text)

    with allure.step("Fill account information"):
        signup.fill_in_account_info(password)
        signup.select_birth_date(day, month, year)
        signup.set_checkboxes()

    with allure.step("Fill address information"):
        signup.fill_address_info(*Data.get_full_address_data())

    take_screenshot(page, "registered_user_data")

    with allure.step(f"Click 'Create Account' and verify '{Data.signed_up_account_info_text}'"):
        signup.click_create_account_button()
        expect(signup.signed_up_account_info_text).to_have_text(Data.signed_up_account_info_text)

    with allure.step(f"Click 'Continue' and verify login as '{user_name}'"):
        signup.click_continue_button()
        expect(home.logged_in_as_text).to_have_text(Data.logged_in_as_text + user_name)