from behave import *
from tests.pages.fashion_site_home_page import fashion_site_home_page


@step("I search for the '{item}'")
def search_products(context, item):
    fashion_site_home_page(context.driver).search_products(item)


@step("I add products to the cart")
def add_to_cart(context):
    fashion_site_home_page(context.driver).add_products_to_cart()
    fashion_site_home_page(context.driver).go_to_cart()
