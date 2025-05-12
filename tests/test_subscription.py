import pytest
import allure

from playwright.sync_api import expect
from pages.home_page import Home
from data.test_data import Data
from utils.tools import take_screenshot

@allure.feature("Subscription")
class TestSubscription:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)

    @allure.title("Verify Subscription in home page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.subscription
    def test_subscription(self, test_setup):
        email = Data.get_random_email()

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Scroll down to footer"):
            self.home.scroll_to_footer()

        with allure.step(f"Verify '{Data.subscription_header_text}' text is visible"):
            expect(self.home.subscription_header_text).to_have_text(Data.subscription_header_text)

        take_screenshot(self.page, "footer")

        with allure.step(f"Fill subscription form with email: {email} and click arrow button"):
            self.home.fill_subscription_email_input(email)
            self.home.click_subscribe_btn()

        with allure.step(f"Verify '{Data.success_subscribe_text}' text is visible"):
            expect(self.home.success_subscribe_text).to_have_text(Data.success_subscribe_text)