import pytest
import allure
from playwright.sync_api import expect

from actions.user_actions import register_user
from pages.home_page import Home
from data.test_data import Data
from utils.tools import take_screenshot

@allure.feature("User Registration")
@allure.severity(allure.severity_level.CRITICAL)
class TestRegisterUser:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)

    @allure.title("Register user")
    @pytest.mark.one
    def test_register_user(self, test_setup):
        register_user(self.page)

        with allure.step(f"Delete account and verify '{Data.account_deleted_text}' message"):
            self.home.click_delete_account_button()
            expect(self.home.account_deleted_text).to_have_text(Data.account_deleted_text)

        take_screenshot(self.page, "account_deleted")