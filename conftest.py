import allure
import pytest

from playwright.sync_api import Playwright
from pages.header_page import Header
from pages.home_page import Home
from pages.signup_login_page import SignUpLoginPage
from data.test_data import Data
from utils.tools import take_screenshot

disable_loggers = []

@pytest.fixture(scope='function')
def new_page(playwright: Playwright, request):
    browser_name = request.config.getoption('--browser_name')
    headless = False if request.config.getoption("--headed") else True

    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.goto('https://www.automationexercise.com')
    yield page
    browser.close()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium')

def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "new_page" in item.funcargs:
            page = item.funcargs["new_page"]

            allure.attach(
                page.screenshot(full_page=True, type='png'),
                name=f"{item.nodeid}.png",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture
def register_user(new_page):
    page = new_page
    header = Header(page)
    home = Home(page)
    signup = SignUpLoginPage(page)

    user_name = Data.random_username()
    email = Data.get_random_email()
    password = Data.random_password()
    day, month, year = Data.random_birth_date()

    home.items_container.wait_for(state="visible")
    header.click_signup_login_btn()
    signup.fill_in_signup_form(user_name, email)
    signup.click_signup_form_btn()
    signup.fill_in_account_info(password)
    signup.select_birth_date(day, month, year)
    signup.set_checkboxes()
    signup.fill_address_info(*Data.get_full_address_data())
    signup.click_create_account_button()
    signup.click_continue_button()

    return email, password, user_name