from behave import *
from tests.pages.my_account_fashion_site_page import my_account_fashion_site_page


@step("Error Message displayed")
def error_login_or_register(context):
    myaccount = my_account_fashion_site_page(context.driver)
    myaccount.verify_login_or_registration_failed()
