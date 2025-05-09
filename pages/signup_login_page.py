import random

from playwright.sync_api import Page

class SignUpLoginPage:
    def __init__(self, page: Page):
        self.page = page
        #Signup
        self.__signup_form = self.page.locator('.signup-form')
        self.__name_input = self.__signup_form.locator('input[type="text"]')
        self.__email_input = self.__signup_form.locator('input[type="email"]')
        self.__signup_form_btn = self.__signup_form.locator('button')
        #Account Information
        self.__signup_account_info_text = self.page.locator('.login-form>.text-center')
        self.__gender_radio_mr = self.page.locator('input[type="radio"][value="Mr"]')
        self.__gender_radio_mrs = self.page.locator('input[type="radio"][value="Mrs"]')
        self.__password_input = self.page.locator('#password')
        self.__day_select = self.page.locator('select#days')
        self.__month_select = self.page.locator('select#months')
        self.__year_select = self.page.locator('select#years')
        self.__newsletter_checkbox = self.page.locator('#newsletter')
        self.__receive_checkbox = self.page.locator('#optin')
        #Address Information
        self.__first_name_input = self.page.locator('#first_name')
        self.__last_name_input = self.page.locator('#last_name')
        self.__company_input = self.page.locator('#company')
        self.__address_1_input = self.page.locator('#address1')
        self.__address_2_input = self.page.locator('#address2')
        self.__country_select = self.page.locator('#country')
        self.__state_input = self.page.locator('#state')
        self.__city_input = self.page.locator('#city')
        self.__zipcode_input = self.page.locator('#zipcode')
        self.__mobile_input = self.page.locator('#mobile_number')
        #Create account
        self.__create_account_button = self.page.locator('button[data-qa="create-account"]')
        self.__signed_up_account_info_text = self.page.locator('h2[data-qa="account-created"]')
        self.__continue_button = self.page.locator('a[class="btn btn-primary"]')

    @property
    def signup_form_container(self):
        return self.__signup_form

    @property
    def signup_account_info_text(self):
        return self.__signup_account_info_text

    @property
    def signed_up_account_info_text(self):
        return self.__signed_up_account_info_text

    def fill_in_signup_form(self, user_name: str, email: str) -> None:
        self.__name_input.fill(user_name)
        self.__email_input.fill(email)

    def click_signup_form_btn(self) -> None:
        self.__signup_form_btn.click()

    def select_random_gender(self) -> None:
        gender = random.choice(["Mr", "Mrs"])
        if gender == "Mr":
            self.__gender_radio_mr.check()
        else:
            self.__gender_radio_mrs.check()
        return gender

    def fill_in_account_info(self, password) -> None:
        self.select_random_gender()
        self.__password_input.fill(password)

    def select_birth_date(self, day: int, month: int, year: int) -> None:
        self.__day_select.select_option(str(day))
        self.__month_select.select_option(str(month))
        self.__year_select.select_option(str(year))

    def set_checkboxes(self) -> None:
        self.__newsletter_checkbox.check()
        self.__receive_checkbox.check()

    def fill_address_info(
            self,
            first_name: str,
            last_name: str,
            company: str,
            address1: str,
            address2: str,
            country: str,
            state: str,
            city: str,
            zipcode: str,
            mobile: str
    ) -> None:
        self.__first_name_input.fill(first_name)
        self.__last_name_input.fill(last_name)
        self.__company_input.fill(company)
        self.__address_1_input.fill(address1)
        self.__address_2_input.fill(address2)
        self.__country_select.select_option(label=country)
        self.__state_input.fill(state)
        self.__city_input.fill(city)
        self.__zipcode_input.fill(zipcode)
        self.__mobile_input.fill(mobile)

    def click_create_account_button(self) -> None:
        self.__create_account_button.click()

    def click_continue_button(self) -> None:
        self.__continue_button.click()
