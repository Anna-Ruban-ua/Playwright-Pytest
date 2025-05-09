from faker import Faker
import random
faker = Faker()

class Data:
    signup_form_text = "New User Signup!"
    signup_account_info_text = "Enter Account Information"
    signed_up_account_info_text = "Account Created!"
    logged_in_as_text = "Logged in as "
    account_deleted_text = "Account Deleted!"

    available_countries = [
        "India",
        "United States",
        "Canada",
        "Australia",
        "Israel",
        "New Zealand",
        "Singapore"
    ]

    @staticmethod
    def get_random_email():
        return f"{faker.user_name()}@testmail.com"

    @staticmethod
    def random_username():
        return faker.user_name()

    @staticmethod
    def random_password():
        return faker.password()

    @staticmethod
    def random_birth_date():
        date = faker.date_of_birth(minimum_age=18, maximum_age=60)
        return date.day, date.month, date.year

    @staticmethod
    def get_full_address_data():
        return (
            faker.first_name(),
            faker.last_name(),
            faker.company(),
            faker.street_address(),
            faker.secondary_address(),
            random.choice(Data.available_countries),
            faker.state(),
            faker.city(),
            faker.zipcode(),
            faker.phone_number()
        )