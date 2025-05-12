import pytest
import allure

from playwright.sync_api import expect
from pages.home_page import Home
from utils.tools import take_screenshot
from pages.header_page import Header
from pages.cases_page import Cases

@allure.feature("Test Cases Page")
class TestCasesPage:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.header = Header(self.page)
        self.home = Home(self.page)
        self.testcases = Cases(self.page)

    @allure.title("Verify Test Cases Page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.navigation
    @pytest.mark.testcases
    def test_testcases_page(self, test_setup):

        with allure.step("Verify homepage is visible"):
            expect(self.home.items_container).to_be_visible()

        with allure.step("Click on 'Test Cases' button"):
            self.header.click_test_cases_btn()

        with allure.step("Verify test cases page is visible"):
            expect(self.testcases.container).to_be_visible()

        take_screenshot(self.page, "test_cases_container")