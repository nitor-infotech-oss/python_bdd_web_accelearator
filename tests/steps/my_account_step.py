from behave import *
from tests.pages.my_account_fashion_site_page import my_account_fashion_site_page
from data_providers.data_provider import DataProvider
from data_providers import json_parser
from tests.utils import common


@step("I register the '{user}' with invalid data")
def user_register(context, user):
    common.go_to(context, page='my-account')
    google_sheet_id = '1KWXC8u1baB_zl_JhC4BJiKL1JZTbB_uDljaIbx4FCNM'
    google_sheet = DataProvider(google_sheet_id=google_sheet_id)
    credentials = google_sheet.read_google_sheet_credentials(user=user)
    my_account_fashion_site_page(context.driver).invalid_user_registration(credentials['username'],
                                                                           credentials['password'])


@step("I register '{user}' with invalid data")
def wrong_user_register(context, user):
    common.go_to(context, page='my-account')
    credentials = json_parser.read_credentials(user=user)
    my_account_fashion_site_page(context.driver).invalid_user_registration(credentials['username'],
                                                                           credentials['password'])


@step("I register the user with valid data")
def user_register(context):
    common.go_to(context, page='my-account')
    email = common.generate_random_email_and_password()['email']
    password = common.generate_random_email_and_password()['password']
    my_account_fashion_site_page(context.driver).valid_user_registration(email, password)


@step("I verify user registered successfully")
def verify_user_register(context):
    my_account_fashion_site_page(context.driver).verify_user_registration()
    my_account_fashion_site_page(context.driver).user_logout()


@step("user log in with '{user}' data")
def login_into_application(context, user):
    common.go_to(context, page='my-account')
    google_sheet_id = '1KWXC8u1baB_zl_JhC4BJiKL1JZTbB_uDljaIbx4FCNM'
    google_sheet = DataProvider(google_sheet_id=google_sheet_id)
    credentials = google_sheet.read_google_sheet_credentials(user=user)
    my_account_fashion_site_page(context.driver).user_login(credentials['username'], credentials['password'])


@step("I verify user logged in successfully")
def verify_user_login(context):
    my_account_fashion_site_page(context.driver).verify_user_login()
    my_account_fashion_site_page(context.driver).user_logout()
